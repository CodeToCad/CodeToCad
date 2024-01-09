from typing import Optional

from codetocad.interfaces import JointInterface

from codetocad.codetocad_types import *
from codetocad.utilities import *
from codetocad.core import *
from codetocad.enums import *


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import Entity
    from . import Sketch


class Joint(JointInterface):
    entity1: EntityOrItsName
    entity2: EntityOrItsName

    def __init__(self, entity1: EntityOrItsName, entity2: EntityOrItsName):
        self.entity1 = entity1
        self.entity2 = entity2

    def translate_landmark_onto_another(self):
        print(
            "translate_landmark_onto_another called:",
        )
        return self

    def pivot(self):
        print(
            "pivot called:",
        )
        return self

    def gear_ratio(self, ratio: float):
        print("gear_ratio called:", ratio)
        return self

    def limit_location_xyz(
        self,
        x: Optional[DimensionOrItsFloatOrStringValue] = None,
        y: Optional[DimensionOrItsFloatOrStringValue] = None,
        z: Optional[DimensionOrItsFloatOrStringValue] = None,
    ):
        print("limit_location_xyz called:", x, y, z)
        return self

    def limit_location_x(
        self,
        min: Optional[DimensionOrItsFloatOrStringValue] = None,
        max: Optional[DimensionOrItsFloatOrStringValue] = None,
    ):
        print("limit_location_x called:", min, max)
        return self

    def limit_location_y(
        self,
        min: Optional[DimensionOrItsFloatOrStringValue] = None,
        max: Optional[DimensionOrItsFloatOrStringValue] = None,
    ):
        print("limit_location_y called:", min, max)
        return self

    def limit_location_z(
        self,
        min: Optional[DimensionOrItsFloatOrStringValue] = None,
        max: Optional[DimensionOrItsFloatOrStringValue] = None,
    ):
        print("limit_location_z called:", min, max)
        return self

    def limit_rotation_xyz(
        self,
        x: Optional[AngleOrItsFloatOrStringValue] = None,
        y: Optional[AngleOrItsFloatOrStringValue] = None,
        z: Optional[AngleOrItsFloatOrStringValue] = None,
    ):
        print("limit_rotation_xyz called:", x, y, z)
        return self

    def limit_rotation_x(
        self,
        min: Optional[AngleOrItsFloatOrStringValue] = None,
        max: Optional[AngleOrItsFloatOrStringValue] = None,
    ):
        print("limit_rotation_x called:", min, max)
        return self

    def limit_rotation_y(
        self,
        min: Optional[AngleOrItsFloatOrStringValue] = None,
        max: Optional[AngleOrItsFloatOrStringValue] = None,
    ):
        print("limit_rotation_y called:", min, max)
        return self

    def limit_rotation_z(
        self,
        min: Optional[AngleOrItsFloatOrStringValue] = None,
        max: Optional[AngleOrItsFloatOrStringValue] = None,
    ):
        print("limit_rotation_z called:", min, max)
        return self

    @classmethod
    def get_dummy_obj(cls):
        from . import Sketch

        instance = Sketch("mySketch")

        edge = instance.create_line(end_at=(0, 5, 0), start_at=(5, 10, 0))

        instance = Sketch("mySketch")

        edge2 = instance.create_line(end_at=(5, 10, 0), start_at=(5, 5, 0))

        return cls(
            entity1="mySketch",
            entity2="mySketch2",
        )