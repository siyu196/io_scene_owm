import bpy
import io_scene_owm.structures.OvertoolsManagement as OvertoolsManagement


class LoadMaterialLibrary(bpy.types.Operator):
    bl_idname = 'overtools.load_library'
    bl_label = 'Load OWM Library'

    def execute(self, context):
        OvertoolsManagement.update_data(True)
        return {'FINISHED'}

    def invoke(self, context, event):
        return self.execute(context)
