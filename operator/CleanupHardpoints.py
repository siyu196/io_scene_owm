import bpy
from io_scene_owm import bpy_helper

class CleanupHardpoints(bpy.types.Operator):
    bl_idname = 'overtools.delete_unused_hardpoints'
    bl_label = 'Delete Unused Hardpoints'

    def execute(self, context):
        # TODO: bpy_helper.clean_hardpoints()
        return {'FINISHED'}

    def invoke(self, context, event):
        return self.execute(context)
