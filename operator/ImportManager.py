import bpy

from io_scene_owm.operator.importers import ImportOWMAT, ImportOWMDL, ImportOWENTITY, ImportOWMAP, ImportOWEFFECT
from io_scene_owm.operator import CleanupHardpoints, CleanupMaterials, LoadMaterialLibrary, SaveMaterialLibrary, UtilityPanel, OvertoolsSettings
import io_scene_owm.structures.OvertoolsManagement as OvertoolsManagement

classes = (
    ImportOWMAT.ImportOvertoolsMaterial,
    ImportOWMDL.ImportOvertoolsModel,
    ImportOWENTITY.ImportOvertoolsEntity,
    ImportOWMAP.ImportOvertoolsMap,
    ImportOWEFFECT.ImportOvertoolsEffect,
    CleanupHardpoints.CleanupHardpoints,
    CleanupMaterials.CleanupMaterials,
    LoadMaterialLibrary.LoadMaterialLibrary,
    SaveMaterialLibrary.SaveMaterialLibrary,
    UtilityPanel.OvertoolsUtilityPanel,
    OvertoolsSettings.OvertoolsInternalSettings
)

import_impl = (
    ImportOWMAT.topbar_impl,
    ImportOWMDL.topbar_impl,
    ImportOWENTITY.topbar_impl,
    ImportOWMAP.topbar_impl,
    ImportOWEFFECT.topbar_impl
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    for impl in import_impl:
        bpy.types.TOPBAR_MT_file_import.append(impl)

    bpy.types.scene.overtools_internal_settings = bpy.props.PointerProperty(type=OvertoolsSettings.OvertoolsInternalSettings)

    bpy.app.handlers.load_post.append(OvertoolsManagement.reset)


def unregister():
    OvertoolsManagement.reset()

    for cls in classes:
        bpy.utils.unregister_class(cls)

    for impl in import_impl:
        bpy.types.TOPBAR_MT_file_import.remove(impl)

    bpy.app.handlers.load_post.remove(OvertoolsManagement.reset)
    bpy.types.scene.overtools_internal_settings = None
