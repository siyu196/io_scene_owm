from io_scene_owm.structures import SettingsBase

class MaterialSettings(SettingsBase):
    import_unknown_textures: bool

    def replicate_with_filename(self, filename): MaterialSettings(filename=filename, **self._asdict())
