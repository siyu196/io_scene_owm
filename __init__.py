bl_info = {
    'name': 'OWM Import',
    'author': 'overtools',
    'version': (3, 0, 0),
    'blender': (2, 80, 0),
    'location': 'File > Import > OWM',
    'description': 'Import TankLib/DataTool OWM files',
    'warning': '',
    'wiki_url': '',
    'tracker_url': 'https://github.com/overtools/io_scene_owm/issues',
    'category': 'Import-Export'
}

from io_scene_owm.operator import ImportManager

def register():
    ImportManager.register()

def unregister():
    ImportManager.unregister()

if __name__ == '__main__':
    register() 
