import bpy
from bpy.props import StringProperty, BoolProperty
from bpy_extras.io_utils import ImportHelper
from io_scene_owm.structures.MaterialSettings import MaterialSettings


class ImportOvertoolsMaterial(bpy.types.Operator, ImportHelper):
    bl_idname = 'import_material.overtools_material'
    bl_label = 'Import Overtools Material (owmat)'
    bl_options = {'UNDO'}

    filename_ext = '.owmat'
    filter_glob: StringProperty(
        default='*.owmat',
        options={'HIDDEN'},
    )

    import_unknown_textures: BoolProperty(
        name='Import Unknown Textures',
        description='Import textures that aren\'t recognized',
        default=True
    )

    def draw(self, context):
        column = self.layout
        column.label(text='Material')
        column.prop(self, 'import_unknown_textures')

    def execute(self, context):
        settings = MaterialSettings(
            filename=self.filepath,
            import_unknown_textures=self.import_unknown_textures
        )
        print(settings)
        return {'FINISHED'}


def topbar_impl(self, context):
    self.layout.operator(ImportOvertoolsMaterial.bl_idname, text='Overtools Material (.owmat)')
