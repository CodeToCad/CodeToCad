from typing import Optional

from codetocad.interfaces import WireInterface

from codetocad.codetocad_types import *
from codetocad.utilities import *
from codetocad.core import *
from codetocad.enums import *


from . import Entity

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import Edge
    from . import Entity
    from . import Vertex
    from . import Part


class Wire(Entity, WireInterface):
    def mirror(
        self,
        mirror_across_entity: EntityOrItsName,
        axis: AxisOrItsIndexOrItsName,
        resulting_mirrored_entity_name: Optional[str] = None,
    ):
        print(
            "mirror called:", mirror_across_entity, axis, resulting_mirrored_entity_name
        )
        return self

    def linear_pattern(
        self,
        instance_count: "int",
        offset: DimensionOrItsFloatOrStringValue,
        direction_axis: AxisOrItsIndexOrItsName = "z",
    ):
        print("linear_pattern called:", instance_count, offset, direction_axis)
        return self

    def circular_pattern(
        self,
        instance_count: "int",
        separation_angle: AngleOrItsFloatOrStringValue,
        center_entity_or_landmark: EntityOrItsName,
        normal_direction_axis: AxisOrItsIndexOrItsName = "z",
    ):
        print(
            "circular_pattern called:",
            instance_count,
            separation_angle,
            center_entity_or_landmark,
            normal_direction_axis,
        )
        return self

    def project(self, project_onto: "Sketch") -> "Projectable":
        from . import Sketch

        print("project called:", project_onto)
        return Sketch("a projected sketch")

    edges: "list[Edge]"
    parent_entity: Optional[EntityOrItsName] = None
    name: str
    description: Optional[str] = None
    native_instance = None

    def __init__(
        self,
        edges: "list[Edge]",
        name: str,
        parent_entity: Optional[EntityOrItsName] = None,
        description: Optional[str] = None,
        native_instance=None,
    ):
        self.edges = edges
        self.parent_entity = parent_entity
        self.name = name
        self.description = description
        self.native_instance = native_instance

    def get_vertices(self) -> "list[Vertex]":
        from . import Vertex

        print(
            "get_vertices called:",
        )
        return [Vertex(location=(0, 0), name="myVertex")]

    def is_closed(self) -> bool:
        print(
            "is_closed called:",
        )
        return True

    def loft(self, other: "Wire", new_part_name: Optional[str] = None) -> "Part":
        from . import Part

        print("loft called:", other, new_part_name)
        return Part("a part")