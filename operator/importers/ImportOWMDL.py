import bpy
from bpy_extras.io_utils import ImportHelper


class ImportOvertoolsModel(bpy.types.Operator, ImportHelper):
    bl_idname = 'import_mesh.overtools_model'
    bl_label = 'Import Overtools Model (owmdl)'
    bl_options = {'UNDO'}


def topbar_impl(self, context):
    self.layout.operator(ImportOvertoolsModel.bl_idname, text="Overtools Model (.owmdl)")
