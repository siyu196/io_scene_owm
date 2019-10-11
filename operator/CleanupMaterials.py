import bpy
import io_scene_owm.structures.OvertoolsManagement as OvertoolsManagement


class CleanupMaterials(bpy.types.Operator):
    bl_idname = 'overtools.delete_unused_materials'
    bl_label = 'Delete Unused Materials'

    def execute(self, context):
        OvertoolsManagement.clean_materials()
        return {'FINISHED'}

    def invoke(self, context, event):
        return self.execute(context)
