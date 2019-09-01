import bpy
from bpy_extras.io_utils import ImportHelper


class ImportOvertoolsMap(bpy.types.Operator, ImportHelper):
    bl_idname = 'import_scene.overtools_map'
    bl_label = 'Import Overtools Map (owmap)'
    bl_options = {'UNDO'}


def topbar_impl(self, context):
    self.layout.operator(ImportOvertoolsMap.bl_idname, text="Overtools Map (.owmap)")
