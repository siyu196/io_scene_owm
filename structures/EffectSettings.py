from io_scene_owm.structures import SettingsBase


class EffectSettings(SettingsBase):
    import_dmce: bool
    import_cece: bool
    import_nece: bool
    import_svce: bool
    scve_line_seed: int
    scve_sound_seed: int
    cleanup_unused_hardpoints: bool
    force_match_framerate: bool
    target_framerate: float
    import_camera: bool

    def replicate_with_filename(self, filename): EffectSettings(filename=filename, **self._asdict())
