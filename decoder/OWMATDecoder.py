# import bpy
from io_scene_owm.structures.binary.MaterialData import MaterialData


def decode_material(settings):
    data = MaterialData.build(settings.filename)
    return data
