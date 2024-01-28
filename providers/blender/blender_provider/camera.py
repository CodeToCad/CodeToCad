from typing import Optional

from codetocad.interfaces import CameraInterface
from codetocad.codetocad_types import *
from codetocad.utilities import *
from codetocad.core import *
from codetocad.enums import *

from providers.blender.blender_provider import (
    blender_definitions,
    Entity,
)
from providers.blender.blender_provider.blender_actions.camera import (
    create_camera,
    set_focal_length,
)
from providers.blender.blender_provider.blender_actions.transformations import (
    rotate_object,
)


class Camera(Entity, CameraInterface):
    name: str
    description: Optional[str] = None

    def __init__(self, name: str, description: Optional[str] = None):
        self.name = name
        self.description = description

    def create_perspective(self):
        create_camera(self.name, type="PERSP")
        return self

    def create_orthogonal(self):
        create_camera(self.name, type="ORTHO")
        return self

    def create_panoramic(self):
        create_camera(self.name, type="PANO")
        return self

    def set_focal_length(self, length):
        set_focal_length(self.name, length)
        return self

    def translate_xyz(
        self,
        x: DimensionOrItsFloatOrStringValue,
        y: DimensionOrItsFloatOrStringValue,
        z: DimensionOrItsFloatOrStringValue,
    ):
        Entity(self.name).translate_xyz(x, y, z)

        return self

    def rotate_xyz(
        self,
        x: AngleOrItsFloatOrStringValue,
        y: AngleOrItsFloatOrStringValue,
        z: AngleOrItsFloatOrStringValue,
    ):
        xAngle = Angle.from_angle_or_its_float_or_string_value(x)
        yAngle = Angle.from_angle_or_its_float_or_string_value(y)
        zAngle = Angle.from_angle_or_its_float_or_string_value(z)

        rotate_object(
            self.name,
            [xAngle, yAngle, zAngle],
            blender_definitions.BlenderRotationTypes.EULER,
        )

        return self

    def is_exists(self) -> bool:
        return Entity(self.name).is_exists()

    def rename(self, new_name: str):
        Entity(self.name).rename(new_name, False)

        self.name = new_name

        return self

    def delete(self):
        Entity(self.name).delete(False)

        return self

    def get_native_instance(self):
        return Entity(self.name).get_native_instance()

    def get_location_world(self) -> "Point":
        return Entity(self.name).get_location_world()

    def get_location_local(self) -> "Point":
        return Entity(self.name).get_location_local()

    def select(self):
        Entity(self.name).select()

        return self
