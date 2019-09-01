import bpy
from bpy_extras.io_utils import ImportHelper


class ImportOvertoolsMaterial(bpy.types.Operator, ImportHelper):
    bl_idname = 'import_material.overtools_material'
    bl_label = 'Import Overtools Material (owmat)'
    bl_options = {'UNDO'}


def topbar_impl(self, context):
    self.layout.operator(ImportOvertoolsMaterial.bl_idname, text="Overtools Material (.owmat)")
