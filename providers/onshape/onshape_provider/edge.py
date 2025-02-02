from typing import Optional
from codetocad.utilities.supported import supported
from codetocad.enums.support_level import SupportLevel
from codetocad.interfaces.entity_interface import EntityInterface
from codetocad.interfaces.projectable_interface import ProjectableInterface
from codetocad.proxy.vertex import Vertex
from codetocad.proxy.landmark import Landmark
from codetocad.interfaces.edge_interface import EdgeInterface
from codetocad.interfaces.vertex_interface import VertexInterface
from codetocad.interfaces.landmark_interface import LandmarkInterface
from providers.onshape.onshape_provider.entity import Entity
from providers.onshape.onshape_provider.vertex import Vertex
from providers.onshape.onshape_provider.landmark import Landmark
from codetocad.codetocad_types import *
from . import Entity
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import Vertex


class Edge(EdgeInterface, Entity):

    @supported(SupportLevel.UNSUPPORTED)
    def mirror(
        self,
        mirror_across_entity: "str|EntityInterface",
        axis: "str|int|Axis",
        resulting_mirrored_entity_name: "str| None" = None,
    ):
        return self

    @supported(SupportLevel.UNSUPPORTED)
    def linear_pattern(
        self,
        instance_count: "int",
        offset: "str|float|Dimension",
        direction_axis: "str|int|Axis" = "z",
    ):
        return self

    @supported(SupportLevel.UNSUPPORTED)
    def circular_pattern(
        self,
        instance_count: "int",
        separation_angle: "str|float|Angle",
        center_entity_or_landmark: "str|EntityInterface",
        normal_direction_axis: "str|int|Axis" = "z",
    ):
        return self

    @supported(SupportLevel.UNSUPPORTED)
    def remesh(self, strategy: "str", amount: "float"):
        return self

    @supported(SupportLevel.UNSUPPORTED)
    def subdivide(self, amount: "float"):
        return self

    @supported(SupportLevel.UNSUPPORTED)
    def decimate(self, amount: "float"):
        return self

    @supported(SupportLevel.UNSUPPORTED)
    def project(self, project_from: "ProjectableInterface") -> "Projectable":
        raise NotImplementedError()

    v1: "Vertex"
    v2: "Vertex"
    parent_entity: Optional[str | Entity] = None
    name: str
    description: Optional[str] = None
    native_instance = None

    def __init__(
        self,
        name: "str",
        v1: "VertexInterface",
        v2: "VertexInterface",
        description: "str| None" = None,
        native_instance=None,
        parent_entity: "str|EntityInterface| None" = None,
    ):
        self.v1 = v1
        self.v2 = v2
        self.parent_entity = parent_entity
        self.name = name
        self.description = description
        self.native_instance = native_instance

    @supported(SupportLevel.UNSUPPORTED)
    def offset(self, distance: "str|float|Dimension") -> "Edge":
        raise NotImplementedError()

    @supported(SupportLevel.UNSUPPORTED)
    def fillet(self, other_edge: "EdgeInterface", amount: "str|float|Angle"):
        return self

    @supported(SupportLevel.UNSUPPORTED)
    def set_is_construction(self, is_construction: "bool"):
        return self

    @supported(SupportLevel.UNSUPPORTED)
    def get_is_construction(self) -> bool:
        raise NotImplementedError()

    @supported(SupportLevel.UNSUPPORTED)
    def create_landmark(
        self,
        landmark_name: "str",
        x: "str|float|Dimension",
        y: "str|float|Dimension",
        z: "str|float|Dimension",
    ) -> "LandmarkInterface":
        print("create_landmark called", f": {landmark_name}, {x}, {y}, {z}")
        return Landmark("name", "parent")

    @supported(SupportLevel.UNSUPPORTED)
    def get_landmark(self, landmark_name: "str|PresetLandmark") -> "LandmarkInterface":
        print("get_landmark called", f": {landmark_name}")
        return Landmark("name", "parent")
