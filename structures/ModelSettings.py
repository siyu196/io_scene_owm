from io_scene_owm.structures.MaterialSettings import MaterialSettings


class ModelSettings(MaterialSettings):
    uv_displacement_x: float
    uv_displacement_y: float
    import_normals: bool
    import_hardpoints: bool
    import_material: bool
    import_skeleton: bool
    import_vertex_color: bool

    def replicate_with_filename(self, filename): ModelSettings(filename=filename, **self._asdict())
