import bpy
from bpy_extras.io_utils import ImportHelper
from bpy.props import StringProperty, IntProperty, FloatProperty, BoolProperty
from io_scene_owm.structures.EffectSettings import EffectSettings


class ImportOvertoolsEffect(bpy.types.Operator, ImportHelper):
    bl_idname = 'import_anim.overtools_effect'
    bl_label = 'Import Overtools Animation Effect (oweffect, owanim)'
    bl_options = {'UNDO'}

    filename_ext = '.owanim'
    filter_glob: StringProperty(
        default='*.owanim;*.oweffect',
        options={'HIDDEN'},
    )

    import_camera: BoolProperty(
        name='Import Camera',
        description='Create a new camera based on the effect',
        default=True
    )

    import_dmce: BoolProperty(
        name='Import DMCE',
        default=True
    )

    import_cece: BoolProperty(
        name='Import CECE',
        default=True
    )

    import_nece: BoolProperty(
        name='Import NECE',
        default=True
    )

    import_svce: BoolProperty(
        name='Import SVCE',
        default=True
    )

    scve_line_seed: IntProperty(
        name='SCVE Line Seed',
        default=1
    )

    scve_sound_seed: IntProperty(
        name='SCVE Sound Seed',
        default=1
    )

    cleanup_unused_hardpoints: BoolProperty(
        name='Cleanup Unused Hardpoints',
        default=1
    )

    force_match_framerate: BoolProperty(
        name='Match Framerate',
        default=True
    )

    target_framerate: FloatProperty(
        name='Target Framerate',
        default=60
    )

    def draw(self, context):
        column = self.layout
        column.label(text='Effect')
        column.prop(self, 'import_camera')
        column.prop(self, 'import_dmce')
        column.prop(self, 'import_cece')
        column.prop(self, 'import_nece')
        column.prop(self, 'import_svce')
        column.prop(self, 'cleanup_unused_hardpoints')
        column.prop(self, 'force_match_framerate')
        column.prop(self, 'target_framerate')

        row = self.layout.row()
        column = row.column(align=False)
        column.label(text='SVCE')
        column.enabled = self.import_svce
        column.prop(self, 'scve_line_seed')
        column.prop(self, 'scve_sound_seed')

    def execute(self, context):
        settings = EffectSettings(
            import_camera=self.import_camera,
            import_dmce=self.import_dmce,
            import_cece=self.import_cece,
            import_nece=self.import_nece,
            import_svce=self.import_svce,
            scve_line_seed=self.scve_line_seed,
            scve_sound_seed=self.svce_sound_seed,
            cleanup_unused_hardpoints=self.cleanup_unused_hardpoints,
            force_match_framerate=self.force_match_framerate,
            target_framerate=self.target_framerate
        )
        print(settings)
        return {'FINISHED'}


def topbar_impl(self, context):
    self.layout.operator(ImportOvertoolsEffect.bl_idname, text="Overtools Effect (.oweffect; .owanim)")
