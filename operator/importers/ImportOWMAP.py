import bpy
from bpy.props import StringProperty, FloatProperty, BoolProperty
from bpy_extras.io_utils import ImportHelper
from io_scene_owm.structures.MapSettings import MapSettings


class ImportOvertoolsMap(bpy.types.Operator, ImportHelper):
    bl_idname = 'import_scene.overtools_map'
    bl_label = 'Import Overtools Map (owmap)'
    bl_options = {'UNDO'}

    filename_ext = '.owmap'
    filter_glob: StringProperty(
        default='*.owmap',
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

    import_instanced_models: BoolProperty(
        name='Import Instanced Models',
        description='Import instances modes, these usually make up the bulk of map geometry',
        default=True
    )

    import_single_models: BoolProperty(
        name='Import Single Models',
        description='Import unique models, often things that are animated or are physics props',
        default=True
    )

    import_sound: BoolProperty(
        name='Import Sound',
        description='Import sound vectors into blender space',
        default=False
    )

    cleanup_map: BoolProperty(
        name='Cleanup Map',
        description='Tries to remove most collision and render-assistance materials and models',
        default=True
    )

    import_sun_lights: BoolProperty(
        name='Sun',
        description='Import sun-type lights',
        default=True
    )

    import_sun_lights: BoolProperty(
        name='Sun',
        description='Import sun-type lights',
        default=True
    )

    import_spot_lights: BoolProperty(
        name='Spot',
        description='Import spot-type lights',
        default=True
    )

    import_lamp_lights: BoolProperty(
        name='Lamp',
        description='Import lamp-type lights',
        default=True
    )

    import_lamp_lights: BoolProperty(
        name='Lamp',
        description='Import lamp-type lights',
        default=True
    )

    use_light_strength: BoolProperty(
        name='Use Light Strength',
        description='Use light strength found in data',
        default=True
    )

    light_value_delta: FloatProperty(
        name='Light Value Offset',
        description='Offset light intensity by this value',
        default=0
    )

    shadow_bias: FloatProperty(
        name='Shadow Soft Bias',
        description='Light size for ray shadow sampling',
        default=0.5
    )

    def draw(self, context):
        column = self.layout
        root_column = column
        column.label(text='Map')
        column.prop(self, 'import_instanced_models')
        column.prop(self, 'import_single_models')
        column.prop(self, 'import_sound')
        column.prop(self, 'cleanup_map')
        row = column.row()
        column = row.column(align=True)
        column.label(text='Lights')
        row = column.row(align=True)
        row.prop(self, 'import_sun_lights', icon='LIGHT_SUN', icon_only=False)
        row.prop(self, 'import_spot_lights', icon='LIGHT_SPOT', icon_only=False)
        row.prop(self, 'import_lamp_lights', icon='LIGHT_POINT', icon_only=False)
        column.prop(self, 'shadow_bias')
        column.prop(self, 'use_light_strength')
        row = column.row()
        row.enabled = self.use_light_strength
        row.prop(self, 'light_value_delta')

        row = root_column.row()
        column = row.column(align=False)
        column.label(text='Mesh')
        column.prop(self, 'import_normals')
        column.prop(self, 'import_hardpoints')
        column.prop(self, 'import_material')
        column.prop(self, 'import_skeleton')
        column.prop(self, 'import_vertex_color')

        row = root_column.row(align=True)
        row.label(text='UV Offset')
        row.prop(self, 'uv_displacement_x')
        row.prop(self, 'uv_displacement_y')

        row = root_column.row()
        column = row.column(align=False)
        column.label(text='Material')
        column.enabled = self.import_material
        column.prop(self, 'import_unknown_textures')

    def execute(self, context):
        settings = MapSettings(
            filename=self.filepath,
            import_unknown_textures=self.import_unknown_textures,
            uv_displacement_x=self.uv_displacement_x,
            uv_displacement_y=self.uv_displacement_y,
            import_normals=self.import_normals,
            import_hardpoints=self.import_hardpoints,
            import_material=self.import_material,
            import_skeleton=self.import_skeleton,
            import_vertex_color=self.import_vertex_color,
            import_instanced_models=self.import_instanced_models,
            import_single_models=self.import_single_models,
            import_sound=self.import_sound,
            import_sun_lights=self.import_sun_lights,
            import_spot_lights=self.import_spot_lights,
            import_lamp_lights=self.import_lamp_lights,
            use_light_strength=self.use_light_strength,
            light_value_delta=self.light_value_delta,
            shadow_bias=self.shadow_bias,
            cleanup_map=self.cleanup_map
        )
        print(settings)
        return {'FINISHED'}


def topbar_impl(self, context):
    self.layout.operator(ImportOvertoolsMap.bl_idname, text="Overtools Map (.owmap)")
