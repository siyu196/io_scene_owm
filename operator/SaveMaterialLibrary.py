import bpy


class SaveMaterialLibrary(bpy.types.Operator):
    bl_idname = 'overtools.save_library'
    bl_label = 'Save OWM Library'

    def execute(self, context):
        # TODO: owm_types.create_overwatch_library()
        return {'FINISHED'}

    def invoke(self, context, event):
        return self.execute(context)
