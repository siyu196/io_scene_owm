import bpy
from bpy.props import StringProperty, FloatProperty, BoolProperty
from bpy_extras.io_utils import ImportHelper
from io_scene_owm.structures.ModelSettings import ModelSettings


class ImportOvertoolsModel(bpy.types.Operator, ImportHelper):
    bl_idname = 'import_mesh.overtools_model'
    bl_label = 'Import Overtools Model (owmdl)'
    bl_options = {'UNDO'}

    filename_ext = '.owmdl'
    filter_glob: StringProperty(
        default='*.owmdl',
        options={'HIDDEN'},
    )

    import_unknown_textures: BoolProperty(
        name='Import Unknown Textures',
        description='Import textures that aren\'t recognized',
        default=True
    )

    uv_displacement_x: FloatProperty(
        name='X',
        description='Offset UV X by this amount',
        default=0.0
    )

    uv_displacement_y: FloatProperty(
        name='Y',
        description='Offset UV Y by this amount',
        default=0.0
    )

    import_normals: BoolProperty(
        name='Import Normals',
        description='Import vertex normals',
        default=True
    )

    import_hardpoints: BoolProperty(
        name='Import Hardpoints',
        description='Import model sockets used by entities',
        default=True
    )

    import_material: BoolProperty(
        name='Import Material',
        description='Import model materials',
        default=True
    )

    import_skeleton: BoolProperty(
        name='Import Skeleton',
        description='Import model animation skeleton',
        default=True
    )

    import_vertex_color: BoolProperty(
        name='Import Colors',
        description='Import vertex colors',
        default=True
    )

    def draw(self, context):
        column = self.layout
        column.label(text='Mesh')
        column.prop(self, 'import_normals')
        column.prop(self, 'import_hardpoints')
        column.prop(self, 'import_material')
        column.prop(self, 'import_skeleton')
        column.prop(self, 'import_vertex_color')

        row = self.layout.row(align=True)
        row.label(text='UV Offset')
        row.prop(self, 'uv_displacement_x')
        row.prop(self, 'uv_displacement_y')

        row = self.layout.row()
        column = row.column(align=False)
        column.label(text='Material')
        column.enabled = self.import_material
        column.prop(self, 'import_unknown_textures')

    def execute(self, context):
        settings = ModelSettings(
            filename=self.filepath,
            import_unknown_textures=self.import_unknown_textures,
            uv_displacement_x=self.uv_displacement_x,
            uv_displacement_y=self.uv_displacement_y,
            import_normals=self.import_normals,
            import_hardpoints=self.import_hardpoints,
            import_material=self.import_material,
            import_skeleton=self.import_skeleton,
            import_vertex_color=self.import_vertex_color
        )
        print(settings)
        return {'FINISHED'}


def topbar_impl(self, context):
    self.layout.operator(ImportOvertoolsModel.bl_idname, text='Overtools Model (.owmdl)')
