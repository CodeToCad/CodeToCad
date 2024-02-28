from typing import Optional
from codetocad.interfaces import EntityInterface
from codetocad.codetocad_types import *
from codetocad.utilities import *
from codetocad.core import *
from codetocad.enums import *
from providers.blender.blender_provider import blender_definitions
from providers.blender.blender_provider.blender_actions.context import (
    apply_dependency_graph,
    select_object,
    update_view_layer,
)
from providers.blender.blender_provider.blender_actions.mesh import (
    get_bounding_box,
    remove_mesh,
)
from providers.blender.blender_provider.blender_actions.modifiers import clear_modifiers
from providers.blender.blender_provider.blender_actions.objects import (
    get_object,
    get_object_local_location,
    get_object_visibility,
    get_object_world_location,
    remove_object,
    set_object_visibility,
    update_object_data_name,
    update_object_landmark_names,
    update_object_name,
)
from providers.blender.blender_provider.blender_actions.transformations import (
    apply_object_transformations,
    rotate_object,
    translate_object,
)


class Entity(EntityInterface):
    name: str
    description: Optional[str] = None
    native_instance = None

    def __init__(
        self, name: "str", description: "str| None" = None, native_instance=None
    ):
        self.name = name
        self.description = description
        self.native_instance = native_instance

    def is_exists(self) -> bool:
        try:
            return get_object(self.name) is not None
        except:  # noqa: E722
            return False

    def rename(
        self, new_name: "str", renamelinked_entities_and_landmarks: "bool" = True
    ):
        assert Entity(new_name).is_exists() is False, f"{new_name} already exists."
        update_object_name(self.name, new_name)
        if renamelinked_entities_and_landmarks:
            update_object_data_name(new_name, new_name)
            update_object_landmark_names(new_name, self.name, new_name)
        self.name = new_name
        return self

    def delete(self, remove_children: "bool" = True):
        remove_object(self.name, remove_children)
        return self

    def is_visible(self) -> bool:
        return get_object_visibility(self.name)

    def set_visible(self, is_visible: "bool"):
        set_object_visibility(self.name, is_visible)
        return self

    def _apply_modifiers_only(self):
        return self.apply(rotation=False, scale=False, location=False, modifiers=True)

    def _apply_rotation_and_scale_only(self):
        return self.apply(rotation=True, scale=True, location=False, modifiers=False)

    def apply(
        self,
        rotation: "bool" = True,
        scale: "bool" = True,
        location: "bool" = False,
        modifiers: "bool" = True,
    ):
        update_view_layer()
        if modifiers and isinstance(self, Part):
            # Only apply modifiers for Blender Objects that have meshes
            apply_dependency_graph(self.name)
            remove_mesh(self.name)
            update_object_data_name(self.name, self.name)
            clear_modifiers(self.name)
        if rotation or scale or location:
            apply_object_transformations(self.name, rotation, scale, location)
        return self

    def get_native_instance(self) -> object:
        return get_object(self.name)

    def get_location_world(self) -> "Point":
        update_view_layer()
        return get_object_world_location(self.name)

    def get_location_local(self) -> "Point":
        update_view_layer()
        return get_object_local_location(self.name)

    def select(self):
        select_object(self.name)
        return self

    @staticmethod
    def _translation_dimension_from_dimension_or_its_float_or_string_value(
        dimension_or_its_float_or_string_value: DimensionOrItsFloatOrStringValue,
        boundary_axis: BoundaryAxis,
    ):
        dimension = Dimension.from_dimension_or_its_float_or_string_value(
            dimension_or_its_float_or_string_value, boundary_axis
        )
        return blender_definitions.BlenderLength.convert_dimension_to_blender_unit(
            dimension
        )

    def translate_xyz(
        self,
        x: "DimensionOrItsFloatOrStringValue",
        y: "DimensionOrItsFloatOrStringValue",
        z: "DimensionOrItsFloatOrStringValue",
    ):
        boundingBox = get_bounding_box(self.name)
        assert (
            boundingBox.x and boundingBox.y and boundingBox.z
        ), "Could not get bounding box"
        xDimension = (
            Entity._translation_dimension_from_dimension_or_its_float_or_string_value(
                x, boundingBox.x
            )
        )
        yDimension = (
            Entity._translation_dimension_from_dimension_or_its_float_or_string_value(
                y, boundingBox.y
            )
        )
        zDimension = (
            Entity._translation_dimension_from_dimension_or_its_float_or_string_value(
                z, boundingBox.z
            )
        )
        translate_object(
            self.name,
            [xDimension, yDimension, zDimension],
            blender_definitions.BlenderTranslationTypes.ABSOLUTE,
        )
        return self

    def translate_x(self, amount: "DimensionOrItsFloatOrStringValue"):
        boundingBox = get_bounding_box(self.name)
        assert boundingBox.x, "Could not get bounding box"
        dimension = (
            Entity._translation_dimension_from_dimension_or_its_float_or_string_value(
                amount, boundingBox.x
            )
        )
        translate_object(
            self.name,
            [dimension, None, None],
            blender_definitions.BlenderTranslationTypes.ABSOLUTE,
        )
        return self

    def translate_y(self, amount: "DimensionOrItsFloatOrStringValue"):
        boundingBox = get_bounding_box(self.name)
        assert boundingBox.y, "Could not get bounding box"
        dimension = (
            Entity._translation_dimension_from_dimension_or_its_float_or_string_value(
                amount, boundingBox.y
            )
        )
        translate_object(
            self.name,
            [None, dimension, None],
            blender_definitions.BlenderTranslationTypes.ABSOLUTE,
        )
        return self

    def translate_z(self, amount: "DimensionOrItsFloatOrStringValue"):
        boundingBox = get_bounding_box(self.name)
        assert boundingBox.z, "Could not get bounding box"
        dimension = (
            Entity._translation_dimension_from_dimension_or_its_float_or_string_value(
                amount, boundingBox.z
            )
        )
        translate_object(
            self.name,
            [None, None, dimension],
            blender_definitions.BlenderTranslationTypes.ABSOLUTE,
        )
        return self

    def rotate_xyz(
        self,
        x: "AngleOrItsFloatOrStringValue",
        y: "AngleOrItsFloatOrStringValue",
        z: "AngleOrItsFloatOrStringValue",
    ):
        xAngle = Angle.from_angle_or_its_float_or_string_value(x)
        yAngle = Angle.from_angle_or_its_float_or_string_value(y)
        zAngle = Angle.from_angle_or_its_float_or_string_value(z)
        rotate_object(
            self.name,
            [xAngle, yAngle, zAngle],
            blender_definitions.BlenderRotationTypes.EULER,
        )
        return self._apply_rotation_and_scale_only()

    def rotate_x(self, rotation: "AngleOrItsFloatOrStringValue"):
        angle = Angle.from_angle_or_its_float_or_string_value(rotation)
        rotate_object(
            self.name,
            [angle, None, None],
            blender_definitions.BlenderRotationTypes.EULER,
        )
        return self._apply_rotation_and_scale_only()

    def rotate_y(self, rotation: "AngleOrItsFloatOrStringValue"):
        angle = Angle.from_angle_or_its_float_or_string_value(rotation)
        rotate_object(
            self.name,
            [None, angle, None],
            blender_definitions.BlenderRotationTypes.EULER,
        )
        return self._apply_rotation_and_scale_only()

    def rotate_z(self, rotation: "AngleOrItsFloatOrStringValue"):
        angle = Angle.from_angle_or_its_float_or_string_value(rotation)
        rotate_object(
            self.name,
            [None, None, angle],
            blender_definitions.BlenderRotationTypes.EULER,
        )
        return self._apply_rotation_and_scale_only()

    def get_bounding_box(self) -> "BoundaryBox":
        return get_bounding_box(self.name)

    def get_dimensions(self) -> "Dimensions":
        dimensions = get_object(self.name).dimensions
        dimensions = [
            Dimension.from_string(
                dimension, blender_definitions.BlenderLength.DEFAULT_BLENDER_UNIT.value
            )
            for dimension in dimensions
        ]
        return Dimensions(dimensions[0], dimensions[1], dimensions[2])
