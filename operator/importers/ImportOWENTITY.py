import bpy
from bpy_extras.io_utils import ImportHelper


class ImportOvertoolsEntity(bpy.types.Operator, ImportHelper):
    bl_idname = 'import_mesh.overtools_entity'
    bl_label = 'Import Overtools Entity (owentity)'
    bl_options = {'UNDO'}


def topbar_impl(self, context):
    self.layout.operator(ImportOvertoolsEntity.bl_idname, text="Overtools Entity (.owentity)")
