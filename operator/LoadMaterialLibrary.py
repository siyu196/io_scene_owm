import bpy

class LoadMaterialLibrary(bpy.types.Operator):
    bl_idname = 'overtools.load_library'
    bl_label = 'Load OWM Library'

    def execute(self, context):
        # TODO: owm_types.update_data(True)
        return {'FINISHED'}

    def invoke(self, context, event):
        return self.execute(context)
