from typing import Optional

import adsk.core, adsk.fusion
from adsk import fusion

from codetocad.interfaces import SketchInterface, ProjectableInterface

from codetocad.codetocad_types import *
from codetocad.utilities import *
from codetocad.core import *
from codetocad.enums import *
from providers.fusion360.fusion360_provider.fusion_actions.curve import create_curve

from .fusion_actions.common import get_sketch


from . import Entity

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import Part
    from . import Entity
    from . import Wire
    from . import Vertex
    from . import Edge


class Sketch(Entity, SketchInterface):
    def project(self, project_onto: "Sketch") -> "ProjectableInterface":
        print("project called:", project_onto)
        from . import Sketch

        return Sketch("a projected sketch")

    def mirror(
        self,
        mirror_across_entity: EntityOrItsName,
        axis: AxisOrItsIndexOrItsName,
        resulting_mirrored_entity_name: Optional[str] = None,
    ):
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

    def create_from_file(self, file_path: str, file_type: Optional[str] = None):
        print("create_from_file called:", file_path, file_type)
        return self

    def export(self, file_path: str, overwrite: bool = True, scale: float = 1.0):
        print("export called:", file_path, overwrite, scale)
        return self

    def translate_xyz(
        self,
        x: DimensionOrItsFloatOrStringValue,
        y: DimensionOrItsFloatOrStringValue,
        z: DimensionOrItsFloatOrStringValue,
    ):
        sketch = get_sketch(self.name)

        for point in sketch.sketchPoints:
            current_origin = point.geometry
            translation_vector = adsk.core.Vector3D.create(current_origin.x + x, current_origin.y + y, current_origin.z + z)
            point.move(translation_vector)

        return self

    def translate_x(self, amount: DimensionOrItsFloatOrStringValue):
        sketch = get_sketch(self.name)

        for point in sketch.sketchPoints:
            current_origin = point.geometry
            translation_vector = adsk.core.Vector3D.create(current_origin.x + amount, current_origin.y, current_origin.z)
            point.move(translation_vector)

        return self

    def translate_y(self, amount: DimensionOrItsFloatOrStringValue):
        sketch = get_sketch(self.name)

        for point in sketch.sketchPoints:
            current_origin = point.geometry
            translation_vector = adsk.core.Vector3D.create(current_origin.x, current_origin.y + amount, current_origin.z)
            point.move(translation_vector)

        return self

    def translate_z(self, amount: DimensionOrItsFloatOrStringValue):
        sketch = get_sketch(self.name)

        for point in sketch.sketchPoints:
            current_origin = point.geometry
            translation_vector = adsk.core.Vector3D.create(current_origin.x, current_origin.y, current_origin.z + amount)
            point.move(translation_vector)

        return self

    def scale_xyz(
        self,
        x: DimensionOrItsFloatOrStringValue,
        y: DimensionOrItsFloatOrStringValue,
        z: DimensionOrItsFloatOrStringValue,
    ):
        print("scale_xyz called:", x, y, z)
        return self

    def scale_x(self, scale: DimensionOrItsFloatOrStringValue):
        print("scale_x called:", scale)
        return self

    def scale_y(self, scale: DimensionOrItsFloatOrStringValue):
        print("scale_y called:", scale)
        return self

    def scale_z(self, scale: DimensionOrItsFloatOrStringValue):
        print("scale_z called:", scale)
        return self

    def scale_x_by_factor(self, scale_factor: float):
        print("scale_x_by_factor called:", scale_factor)
        return self

    def scale_y_by_factor(self, scale_factor: float):
        print("scale_y_by_factor called:", scale_factor)
        return self

    def scale_z_by_factor(self, scale_factor: float):
        print("scale_z_by_factor called:", scale_factor)
        return self

    def scale_keep_aspect_ratio(
        self, scale: DimensionOrItsFloatOrStringValue, axis: AxisOrItsIndexOrItsName
    ):
        print("scale_keep_aspect_ratio called:", scale, axis)
        return self

    name: str
    curve_type: Optional["CurveTypes"] = None
    description: Optional[str] = None
    native_instance = None

    def __init__(
        self,
        name: str,
        curve_type: Optional["CurveTypes"] = None,
        description: Optional[str] = None,
        native_instance=None,
    ):
        self.name = name
        self.curve_type = curve_type
        self.description = description
        self.native_instance = native_instance
        self.resolution = 4

    def clone(self, new_name: str, copy_landmarks: bool = True) -> "Sketch":
        print("clone called:", new_name, copy_landmarks)
        return Sketch("a sketch")

    def revolve(
        self,
        angle: AngleOrItsFloatOrStringValue,
        # about_entity_or_landmark: EntityOrItsName,
        axis,
    ) -> "Part":
        from . import Part

        app = adsk.core.Application.get()
        design = app.activeProduct
        root_comp = design.rootComponent
        sketches = root_comp.sketches;
        xyPlane = root_comp.xYConstructionPlane;
        sketch = sketches.add(xyPlane)

        # revolve_axes = design.rootComponent.constructionAxes
        # axis_input = revolve_axes.createInput()
        # axis_input.setByLine(adsk.core.InfiniteLine3D.create(adsk.core.Point3D.create(0), axis))
        # axis_input.setByTwoPoints(adsk.core.Point3D.create(0), axis)
        # revolve_axis = revolve_axes.add(axis_input)
        # revolve_axis = revolve_axes.add(axis_input)

        axis_line = sketch.sketchCurves.sketchLines
        revolve_axis = axis_line.addByTwoPoints(adsk.core.Point3D.create(0, 0, 0), axis)

        sketch = get_sketch(self.name)

        operation = adsk.fusion.FeatureOperations.NewBodyFeatureOperation

        revolveFeatures = root_comp.features.revolveFeatures
        input = revolveFeatures.createInput(sketch.profiles.item(0), revolve_axis, operation)
        angle = adsk.core.ValueInput.createByReal(angle)
        input.setAngleExtent(False, angle)
        revolveFeature = revolveFeatures.add(input)

        body = design.rootComponent.bRepBodies.item(design.rootComponent.bRepBodies.count - 1)
        body.name = self.name

        return Part(self.name)

    def twist(
        self,
        angle: AngleOrItsFloatOrStringValue,
        screw_pitch: DimensionOrItsFloatOrStringValue,
        iterations: "int" = 1,
        axis: AxisOrItsIndexOrItsName = "z",
    ):
        print("twist called:", angle, screw_pitch, iterations, axis)
        return self

    def extrude(self, length: DimensionOrItsFloatOrStringValue) -> "Part":
        from . import Part

        app = adsk.core.Application.get()

        design = app.activeProduct
        rootComp = design.rootComponent

        sketch = get_sketch(self.name)
        prof = sketch.profiles.item(0)
        extrudes = rootComp.features.extrudeFeatures
        extInput = extrudes.createInput(prof, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)

        distance = adsk.core.ValueInput.createByReal(length)
        extInput.setDistanceExtent(False, distance)
        extInput.isSolid = True
        ext = extrudes.add(extInput)

        body = design.rootComponent.bRepBodies.item(design.rootComponent.bRepBodies.count - 1)
        body.name = self.name

        return Part("a part")

    def sweep(
        self, profile_name_or_instance: SketchOrItsName, fill_cap: bool = True
    ) -> "Part":
        from . import Part

        print("sweep called:", profile_name_or_instance, fill_cap)
        return Part("a part")

    def offset(self, radius: DimensionOrItsFloatOrStringValue):
        print("offset called:", radius)
        return self

    def profile(self, profile_curve_name: str):
        print("profile called:", profile_curve_name)
        return self

    def create_text(
        self,
        text: str,
        font_size: DimensionOrItsFloatOrStringValue = 1.0,
        bold: bool = False,
        italic: bool = False,
        underlined: bool = False,
        character_spacing: "int" = 1,
        word_spacing: "int" = 1,
        line_spacing: "int" = 1,
        font_file_path: Optional[str] = None,
    ):
        print(
            "create_text called:",
            text,
            font_size,
            bold,
            italic,
            underlined,
            character_spacing,
            word_spacing,
            line_spacing,
            font_file_path,
        )
        return self

    def create_from_vertices(
        self, points: list[PointOrListOfFloatOrItsStringValueOrVertex]
    ) -> "Wire":
        # is_closed = False
        # if len(parsed_points) > 1 and parsed_points[0] == parsed_points[-1]:
        #     is_closed = True
        #     parsed_points = parsed_points[:-1]

        # curve_data, parsed_points = create_curve(self.name, points)


        wire = Wire(points, create_uuid_like_id(), self.name)
        return wire

    def create_point(self, point: PointOrListOfFloatOrItsStringValue) -> "Vertex":
        print("create_point called:", point)
        return None

    def create_line(
        self,
        start_at: PointOrListOfFloatOrItsStringValueOrVertex,
        end_at: PointOrListOfFloatOrItsStringValueOrVertex,
    ) -> "Edge":
        from . import Edge

        print("create_line called:", start_at, end_at)
        return Edge.get_dummy_edge()

    def create_circle(self, radius: DimensionOrItsFloatOrStringValue) -> "Wire":
        from .fusion_actions import circle

        app = adsk.core.Application.get()
        design = app.activeProduct
        rootComp = design.rootComponent

        sketches = rootComp.sketches
        xyPlane = rootComp.xYConstructionPlane
        sketch = sketches.add(xyPlane)
        sketch.name = self.name

        radius = Dimension.from_dimension_or_its_float_or_string_value(radius)
        points = circle.get_circle_points(radius, self.resolution)
        points = [adsk.core.Point3D.create(point.x.value, point.y.value, point.z.value) for point in points]

        control_points = adsk.core.ObjectCollection_create()
        for point in points:
            control_points.add(point)

        spline = sketch.sketchCurves.sketchFittedSplines.add(control_points)
        return None

    def create_ellipse(
        self,
        radius_minor: DimensionOrItsFloatOrStringValue,
        radius_major: DimensionOrItsFloatOrStringValue,
    ) -> "Wire":
        from . import Wire

        radius_minor = Dimension.from_dimension_or_its_float_or_string_value(
            radius_minor
        )
        radius_major = Dimension.from_dimension_or_its_float_or_string_value(
            radius_major
        )

        is_minor_lesser = radius_minor < radius_major

        wire = self.create_circle(radius_minor if is_minor_lesser else radius_major)

        if is_minor_lesser:
            self.scale_y(radius_major * 2)
        else:
            self.scale_x(radius_minor * 2)

        return wire

    def create_arc(
        self,
        # start_at: PointOrListOfFloatOrItsStringValueOrVertex,
        # end_at: PointOrListOfFloatOrItsStringValueOrVertex,
        radius: DimensionOrItsFloatOrStringValue,
        flip: Optional[bool] = False,
    ) -> "Wire":
        app = adsk.core.Application.get()
        design = app.activeProduct
        rootComp = design.rootComponent
        sketches = rootComp.sketches
        xyPlane = rootComp.xYConstructionPlane

        sketch = sketches.add(xyPlane)
        sketch.name = self.name

        center = adsk.core.Point3D.create(0, 0, 0)
        circle = sketch.sketchCurves.sketchCircles
        circle.addByCenterRadius(center, radius)

        trim_line = sketch.sketchCurves.sketchLines.addByTwoPoints(
            adsk.core.Point3D.create(center.x - radius, center.y, 0),
            adsk.core.Point3D.create(center.x + radius, center.y, 0)
        )

        return None

    def create_rectangle(
        self,
        length: DimensionOrItsFloatOrStringValue,
        width: DimensionOrItsFloatOrStringValue,
    ) -> "Wire":
        half_length = (
            Dimension.from_dimension_or_its_float_or_string_value(length, None) / 2
        )
        half_width = (
            Dimension.from_dimension_or_its_float_or_string_value(width, None) / 2
        )
        left_top = Point(half_length * -1, half_width, Dimension(0))
        left_bottom = Point(half_length * -1, half_width * -1, Dimension(0))
        right_bottom = Point(half_length, half_width * -1, Dimension(0))
        right_top = Point(half_length, half_width, Dimension(0))

        points = [left_top, left_bottom, right_bottom, right_top, left_top]

        app = adsk.core.Application.get()
        design = app.activeProduct
        rootComp = design.rootComponent
        sketches = rootComp.sketches
        xyPlane = rootComp.xYConstructionPlane

        sketch = sketches.add(xyPlane)
        sketch.name = self.name

        sketchLines = sketch.sketchCurves.sketchLines
        for i in range(len(points) - 1):
            start = adsk.core.Point3D.create(points[i].x.value, points[i].y.value, points[i].z.value)
            end = adsk.core.Point3D.create(points[i + 1].x.value, points[i + 1].y.value, points[i + 1].z.value)
            sketchLines.addByTwoPoints(start, end)

        # startPoint = adsk.core.Point3D.create(0, 0, 0)
        # endPoint = adsk.core.Point3D.create(width, length, 0)
        # sketchLines.addTwoPointRectangle(startPoint, endPoint)

        return None

    def create_lines(
        self,
        points,
    ) -> "Wire":
        app = adsk.core.Application.get()
        design = app.activeProduct
        rootComp = design.rootComponent
        sketches = rootComp.sketches
        xyPlane = rootComp.xYConstructionPlane

        sketch = sketches.add(xyPlane)
        sketch.name = self.name

        lines = sketch.sketchCurves.sketchLines

        for i in range(len(points) - 1):
            start = points[i]
            end = points[i + 1]
            lines.addByTwoPoints(start, end)

        # startPoint = adsk.core.Point3D.create(0, 0, 0)
        # endPoint = adsk.core.Point3D.create(width, length, 0)
        # sketchLines.addTwoPointRectangle(startPoint, endPoint)

        return None

    def create_polygon(
        self,
        number_of_sides: "int",
        length: DimensionOrItsFloatOrStringValue,
        width: DimensionOrItsFloatOrStringValue,
    ) -> "Wire":
        from . import Wire, Edge

        print("create_polygon called:", number_of_sides, length, width)
        return Wire(edges=[Edge(v1=(0, 0), v2=(5, 5), name="myEdge")], name="myWire")

    def create_trapezoid(
        self,
        length_upper: DimensionOrItsFloatOrStringValue,
        length_lower: DimensionOrItsFloatOrStringValue,
        height: DimensionOrItsFloatOrStringValue,
    ) -> "Wire":
        from . import Wire, Edge

        print("create_trapezoid called:", length_upper, length_lower, height)
        return Wire(edges=[Edge(v1=(0, 0), v2=(5, 5), name="myEdge")], name="myWire")

    def create_spiral(
        self,
        number_of_turns: "int",
        height: DimensionOrItsFloatOrStringValue,
        radius: DimensionOrItsFloatOrStringValue,
        is_clockwise: bool = True,
        radius_end: Optional[DimensionOrItsFloatOrStringValue] = None,
    ) -> "Wire":
        from . import Wire, Edge

        print(
            "create_spiral called:",
            number_of_turns,
            height,
            radius,
            is_clockwise,
            radius_end,
        )
        return Wire(edges=[Edge(v1=(0, 0), v2=(5, 5), name="myEdge")], name="myWire")
