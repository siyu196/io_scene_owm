import bpy
from io_scene_owm import bpy_helper


class CleanupMaterials(bpy.types.Operator):
    bl_idname = 'overtools.delete_unused_materials'
    bl_label = 'Delete Unused Materials'

    def execute(self, context):
        # TODO: bpy_helper.clean_materials()
        return {'FINISHED'}

    def invoke(self, context, event):
        return self.execute(context)
