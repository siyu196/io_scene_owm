from io_scene_owm.structures.SettingsBase import OvertoolsSettingsBase


class MaterialSettings(OvertoolsSettingsBase):
    import_unknown_textures: bool

    def replicate_with_filename(self, filename): MaterialSettings(filename=filename, **self._asdict())
