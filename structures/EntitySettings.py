from io_scene_owm.structures import ModelSettings

class EntitySettings(ModelSettings):
    import_subentities: bool

    def replicate_with_filename(self, filename): EntitySettings(filename=filename, **self._asdict())
