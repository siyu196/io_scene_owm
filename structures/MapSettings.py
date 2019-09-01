from io_scene_owm.structures.ModelSettings import ModelSettings


class MapSettings(ModelSettings):
    import_instanced_models: bool
    import_single_models: bool
    import_sound: bool
    import_sun_lights: bool
    import_spot_lights: bool
    import_lamp_lights: bool
    use_light_strength: bool
    light_value_delta: float
    shadow_bias: float
    cleanup_map: bool

    def replicate_with_filename(self, filename): MapSettings(filename=filename, **self._asdict())
