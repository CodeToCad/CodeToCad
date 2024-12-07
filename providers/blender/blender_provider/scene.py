from codetocad.interfaces.exportable_interface import ExportableInterface
from codetocad.utilities.supported import supported
from codetocad.enums.support_level import SupportLevel
from codetocad.proxy.entity import Entity
from codetocad.interfaces.scene_interface import SceneInterface
from codetocad.interfaces.entity_interface import EntityInterface
from codetocad.proxy.part import Part
from codetocad.utilities import get_absolute_filepath
from providers.blender.blender_provider.blender_actions.collections import (
    assign_object_to_collection,
    create_collection,
    get_collection,
    remove_collection,
    remove_object_from_collection,
)
from providers.blender.blender_provider.blender_actions.context import (
    get_selected_objects,
)
from providers.blender.blender_provider.blender_actions.objects import (
    set_object_visibility,
)
from providers.blender.blender_provider.blender_actions.scene import (
    add_hdr_texture,
    get_scene,
    set_background_location,
    set_default_unit as blender_actions_set_default_unit,
)
from providers.blender.blender_provider.blender_definitions import BlenderLength
from codetocad.codetocad_types import *


class Scene(SceneInterface):

    def __init__(self, name: "str| None" = None, description: "str| None" = None):
        # Blender's default Scene name is "Scene"
        self.name = name or "Scene"
        self.description = description

    @staticmethod
    @supported(SupportLevel.SUPPORTED)
    def default() -> "Scene":
        return Scene()

    @supported(SupportLevel.PLANNED)
    def create(self):
        raise NotImplementedError()
        return self

    @supported(SupportLevel.PLANNED)
    def delete(self):
        raise NotImplementedError()
        return self

    @supported(SupportLevel.PLANNED)
    def is_exists(self) -> bool:
        raise NotImplementedError()
        return

    @supported(SupportLevel.SUPPORTED)
    def get_selected_entity(self) -> "EntityInterface":
        return Entity(get_selected_objects()[0].name)

    @supported(SupportLevel.UNSUPPORTED)
    def export(
        self,
        file_path: "str",
        entities: "list[ExportableInterface]",
        overwrite: "bool" = True,
        scale: "float" = 1.0,
    ):
        for entity in entities:
            part = entity
            if isinstance(part, str):
                part = Part(part)
            part.export(file_path, overwrite, scale)
        return self

    @supported(SupportLevel.SUPPORTED)
    def set_default_unit(self, unit: "str|LengthUnit"):
        if isinstance(unit, str):
            unit = LengthUnit.from_string(unit)
        blenderUnit = BlenderLength.from_length_unit(unit)
        blender_actions_set_default_unit(blenderUnit, self.name)
        return self

    @supported(SupportLevel.SUPPORTED)
    def create_group(self, name: "str"):
        create_collection(name, self.name)
        return self

    @supported(SupportLevel.SUPPORTED)
    def delete_group(self, name: "str", remove_children: "bool"):
        remove_collection(
            name=name, scene_name=self.name, remove_children=remove_children
        )
        return self

    @supported(SupportLevel.SUPPORTED)
    def remove_from_group(self, entity: "EntityInterface", group_name: "str"):
        remove_object_from_collection(
            blender_object=entity.get_native_instance(),
            blender_collection=get_collection(group_name, self.name),
        )
        return self

    @supported(SupportLevel.SUPPORTED)
    def assign_to_group(
        self,
        entities: "list[EntityInterface]",
        group_name: "str",
        remove_from_other_groups: "bool| None" = True,
    ):
        for entity in entities:
            assign_object_to_collection(
                blender_object=entity.get_native_instance(),
                blender_collection=get_collection(group_name, self.name),
                remove_from_other_groups=remove_from_other_groups or True,
            )
        return self

    @supported(SupportLevel.SUPPORTED)
    def set_visible(self, entities: "list[EntityInterface]", is_visible: "bool"):
        for entity in entities:
            set_object_visibility(entity.get_native_instance(), is_visible)
        return self

    @supported(SupportLevel.PARTIAL, "Only environment textures are supported.")
    def set_background_image(
        self,
        file_path: "str",
        location_x: "str|float|Dimension| None" = 0,
        location_y: "str|float|Dimension| None" = 0,
    ):
        absoluteFilePath = get_absolute_filepath(file_path)
        blender_scene = get_scene(self.name)
        add_hdr_texture(blender_scene, absoluteFilePath)
        x = BlenderLength.convert_dimension_to_blender_unit(
            Dimension.from_string(location_x or 0)
        ).value
        y = BlenderLength.convert_dimension_to_blender_unit(
            Dimension.from_string(location_y or 0)
        ).value
        set_background_location(blender_scene, x, y)
        return self
