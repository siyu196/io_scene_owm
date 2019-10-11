import bpy
from io_scene_owm.operator import LoadMaterialLibrary, SaveMaterialLibrary, CleanupMaterials


class OvertoolsUtilityPanel(bpy.types.Panel):
    bl_idname = 'OBJECT_PT_select'
    bl_label = 'OWM Utilities'
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = 'scene'

    @classmethod
    def poll(cls, context): return True

    def draw_header(self, context): pass

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator(LoadMaterialLibrary.bl_idname, text='Load Material Library', icon='LINK_BLEND')
        row.operator(SaveMaterialLibrary.bl_idname, text='Save Material Library', icon='APPEND_BLEND')
        row = layout.row()
        row.prop(bpy.context.scene.overtools_internal_settings, 'b_logsalot', text='Log Map Progress')
        row.prop(bpy.context.scene.overtools_internal_settings, 'b_download', text='Always Download Library')

        box = layout.box()
        box.label(text='Cleanup')
        row = box.row()
        row.operator(CleanupMaterials.bl_idname, text='Unused Materials', icon='MATERIAL')
