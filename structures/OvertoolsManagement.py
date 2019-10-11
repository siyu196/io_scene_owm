import os
from urllib.request import urlopen
import json
import bpy
import traceback


DefaultTextureTypesById = {}
DefaultTextureTypes = {
    'Mapping': {},
    'Alias': {},
    'Env': {},
    'Color': [],
    'Active': [],
    'NodeGroups': {
        'Default': 'OWM: Physically Based Shading'
    }
}
TextureTypes = DefaultTextureTypes

LOADED_LIBRARY_VERSION = 0
ALWAYS_DOWNLOAD = False
LIBRARY_STATE = 0  # 0 = Uninitialized, 1 = Linked, 2 = Loaded
LIBRARY_STATE_ENUM = ["UNINITIALIZED", "LINKED", "LOADED"]
LIBRARY_BRANCH = "rewrite"


def clean_materials():
    for mat in bpy.data.materials:
        if mat.users == 0:
            print('[owm]: removed material: {}'.format(mat.name))
            bpy.data.materials.remove(mat)
    bpy.context.view_layer.update()
    for tex in bpy.data.textures:
        if tex.users == 0:
            print('[owm]: removed texture: {}'.format(tex.name))
            bpy.data.textures.remove(tex)
    bpy.context.view_layer.update()


def format_exc(e):
    return ''.join(traceback.format_exception(type(e), e, e.__traceback__))


def reset():
    global DefaultTextureTypes, TextureTypes, LOADED_LIBRARY_VERSION, ALWAYS_DOWNLOAD, LIBRARY_STATE, LIBRARY_STATE_ENUM, LOG_ALOT
    print('[owm] resetting settings')
    TextureTypes = DefaultTextureTypes
    LOADED_LIBRARY_VERSION = 0
    LIBRARY_STATE = bpy.context.scene.overtools_internal_settings.i_library_state
    print("[owm] LIBRARY_STATE: %s" % (LIBRARY_STATE_ENUM[LIBRARY_STATE]))
    ALWAYS_DOWNLOAD = bpy.context.scene.overtools_internal_settings.b_download
    print("[owm] ALWAYS_DOWNLOAD: %d" % (ALWAYS_DOWNLOAD))
    LOG_ALOT = bpy.context.scene.overtools_internal_settings.b_logsalot
    print("[owm] LOG_ALOT: %d" % (LOG_ALOT))


def download(src, dst):
    try:
        print('[owm] trying to download %s' % (src))
        with urlopen(src) as res:
            data = res.read()
            if os.path.exists(dst):
                if os.path.exists(dst + '.bak'):
                    os.remove(dst + '.bak')
                os.rename(dst, dst + '.bak')
            with open(dst, 'w+b') as f:
                f.write(data)
    except BaseException as e:
        print('[owm] failed to download %s: %s' % (src, format_exc(e)))


def update_data(is_editing=False):
    print('[owm] trying to update library file')
    global LOADED_LIBRARY_VERSION, LIBRARY_BRANCH
    v = LOADED_LIBRARY_VERSION
    try:
        with open(get_library_version_path()) as f:
            v = int(f.readline().strip())
            LOADED_LIBRARY_VERSION = v
            with urlopen('https://raw.githubusercontent.com/overtools/io_scene_owm/%s/LIBRARY_VERSION' % LIBRARY_BRANCH) as rF:
                data = rF.read()
                rV = int(data.decode('ascii').split('\n')[0].strip())
                print('[owm] local version %s, remote version %s' % (v, rV))
                if rV > v or ALWAYS_DOWNLOAD:
                    download('https://raw.githubusercontent.com/overtools/io_scene_owm/%s/library.blend' % LIBRARY_BRANCH, get_library_path())
                    download('https://raw.githubusercontent.com/overtools/io_scene_owm/%s/texture-map.json' % LIBRARY_BRANCH, get_texture_type_path())
                    v = rV
    except BaseException as e:
        print('[owm] failed to update: %s' % (format_exc(e)))

    load_data(is_editing)
    if v > LOADED_LIBRARY_VERSION or ALWAYS_DOWNLOAD:
        LOADED_LIBRARY_VERSION = v
        download('https://raw.githubusercontent.com/overtools/io_scene_owm/%s/LIBRARY_VERSION' % LIBRARY_BRANCH, get_library_version_path())


def get_library_path():
    return os.path.join(os.path.dirname(__file__), 'library.blend')


def get_library_version_path():
    return os.path.join(os.path.dirname(__file__), 'LIBRARY_VERSION')


def get_texture_type_path():
    return os.path.join(os.path.dirname(__file__), 'texture-map.json')


def create_overwatch_shader(is_editing=False):
    global LIBRARY_STATE, LIBRARY_STATE_ENUM
    print('[owm] attempting to import shaders (link = %d)' % (is_editing))
    if LIBRARY_STATE == 0:
        LIBRARY_STATE = int(is_editing) + 1
    if LIBRARY_STATE == 2:
        is_editing = True
        print('[owm] library state is LOADED, loading files directly')
    print('[owm] LIBRARY_STATE = %s' % (LIBRARY_STATE_ENUM[LIBRARY_STATE]))
    bpy.context.scene.overtools_internal_settings.i_library_state = LIBRARY_STATE
    path = get_library_path()
    with bpy.data.libraries.load(path, link=not is_editing, relative=True) as (data_from, data_to):
        data_to.node_groups = [node_name for node_name in data_from.node_groups if node_name not in bpy.data.node_groups and node_name.startswith('OWM: ')]
        if len(data_to.node_groups) > 0:
            print('[owm] imported node groups: %s' % (', '.join(data_to.node_groups)))
    blocks = set([node for node in bpy.data.node_groups if node.name.startswith('OWM: ')])
    for block in blocks:
        bpy.data.node_groups[block.name].use_fake_user = True


def create_overwatch_library():
    global LIBRARY_STATE, LIBRARY_STATE_ENUM
    print('[owm] LIBRARY_STATE = %s' % (LIBRARY_STATE_ENUM[LIBRARY_STATE]))
    if LIBRARY_STATE != 2:
        print('[owm] library is locked; %s' % ("load library first" if LIBRARY_STATE == 0 else "blend file is tainted"))
        return
    path = get_library_path()
    print('[owm] attempting to export shaders')
    blocks = set([node for node in bpy.data.node_groups if node.name.startswith('OWM: ')])
    for block in blocks:
        bpy.data.node_groups[block.name].use_fake_user = True
    if len(blocks) > 0:
        print('[owm] exported node groups: %s' % (', '.join(map(lambda x: x.name, blocks))))
    bpy.data.libraries.write(path, blocks, fake_user=True, relative_remap=True, compress=True)
    print('[owm] saved %s' % (path))


def load_data(is_editing=False):
    global TextureTypesById, TextureTypes
    print('[owm] attempting to load texture info')
    try:
        with open(get_texture_type_path()) as f:
            TextureTypes = json.load(f)
            TextureTypesById = {}
            for fname, tdata in TextureTypes['Mapping'].items():
                TextureTypesById[tdata[2]] = fname
                print('[owm] %s = %s' % (fname, json.dumps(tdata)))
        for node in [node for node in bpy.data.node_groups if node.users == 0 and node.name.startswith('OWM: ')]:
            print('[owm] removing unused node group: %s' % (node.name))
            bpy.data.node_groups.remove(node)
        create_overwatch_shader(is_editing)
    except BaseException as e:
        print('[owm] failed to load texture types: %s' % (format_exc(e)))
