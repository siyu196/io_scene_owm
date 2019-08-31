from io_scene_owm.structures import ModelSettings

class MapSettings(ModelSettings):
    import_instanced_models: bool
    import_single_models: bool
    import_sun_lights: bool
    import_spot_lights: bool
    import_lamp_lights: bool
    light_value_delta: float
    use_light_strength: bool
    shadow_bias: float
    cleanup_cleanup: bool
    import_sound: bool

    def replicate_with_filename(self, filename): MapSettings(filename=filename, **self._asdict())
