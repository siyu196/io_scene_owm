import bpy
from bpy_extras.io_utils import ImportHelper


class ImportOvertoolsEffect(bpy.types.Operator, ImportHelper):
    bl_idname = 'import_anim.overtools_effect'
    bl_label = 'Import Overtools Animation Effect (oweffect, owanim)'
    bl_options = {'UNDO'}


def topbar_impl(self, context):
    self.layout.operator(ImportOvertoolsEffect.bl_idname, text="Overtools Effect (.oweffect; .owanim)")
