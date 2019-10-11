import bpy
from bpy.props import BoolProperty, IntProperty
import io_scene_owm.structures.OvertoolsManagement as OvertoolsManagement


class OvertoolsInternalSettings(bpy.types.PropertyGroup):
    b_logsalot: BoolProperty(update=lambda self, context: self.update_logs_alot(context))
    b_download: BoolProperty(update=lambda self, context: self.update_download(context))
    i_library_state: IntProperty(update=lambda self, context: self.dummy(context))

    def update_logs_alot(self, context):
        OvertoolsManagement.LOG_ALOT = self.b_logsalot
        pass

    def update_download(self, context):
        OvertoolsManagement.ALWAYS_DOWNLOAD = self.b_download
        pass

    def dummy(self, context): pass
