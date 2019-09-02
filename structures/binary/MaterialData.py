from io_scene_owm.structures.binary import BinaryHelper
from enum import Enum
from typing import NamedTuple
import os.path

HEADER_FORMAT = ['<HHQ']
MATERIAL_TYPE_FORMAT = ['<I']
MATERIAL_HEADER_FORMAT = ['<Ii']
ID_FORMAT = ['<Q']
MATERIAL_FORMAT = [str, '<I']
MODELLOOK_FORMAT = [str]


class MaterialType(Enum):
    Material = 0
    ModelLook = 1


class MaterialInfo(NamedTuple):
    id: int
    count: int
    textures: list
    shader: int


class MaterialData(NamedTuple):
    materials: list

    @classmethod
    def build(cls, filepath):
        materials = list()
        with BinaryHelper.open_stream(filepath) as stream:
            major, minor, count = BinaryHelper.read_fmt_flat(stream, HEADER_FORMAT)
            if major >= 2 and minor >= 0:
                material_type = MaterialType(BinaryHelper.read_fmt_flat(stream, MATERIAL_TYPE_FORMAT))
                if material_type == MaterialType.Material:
                    shader, id_count = BinaryHelper.read_fmt_flat(stream, MATERIAL_HEADER_FORMAT)
                    ids = []
                    for i in range(id_count):
                        ids.append(BinaryHelper.read_fmt_flat(stream, ID_FORMAT))
                    textures = []
                    for i in range(count):
                        texture, texture_type = BinaryHelper.read_fmt_flat(stream, MATERIAL_FORMAT)
                        textures += [(BinaryHelper.normalize_path(os.path.join(filepath, texture)), 0, texture_type)]
                    else:
                        materials = []
                        for mat_id in ids:
                            materials.append(MaterialInfo(
                                id=mat_id,
                                count=len(textures),
                                textures=textures,
                                shader=shader
                            ))
                elif material_type == MaterialType.ModelLook:
                    materials = []
                    for i in range(count):
                        material_file = BinaryHelper.read_fmt_flat(stream, MODELLOOK_FORMAT)
                        materials += MaterialData.build(BinaryHelper.normalize_path(os.path.join(filepath, material_file))).materials
            else:
                raise Exception('Unsupported file')
        return MaterialData(
            materials=materials
        )
