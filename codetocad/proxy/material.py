# THIS IS AN AUTO-GENERATE FILE.
# DO NOT EDIT MANUALLY.
# Please run development/capabilities_json_to_python/capabilities_to_py.sh to generate this file.
# Copy this file and remove this header to create a new CodeToCAD Provider.

from codetocad.codetocad_types import *

from typing import Self


from codetocad.providers import get_provider

from codetocad.interfaces.material_interface import MaterialInterface


class Material(
    MaterialInterface,
):
    """
    Materials affect the appearance and simulation properties of the parts.

    NOTE: This is a proxy - calling this returns an instance of a registered provider.
    Register a provider using the `register()` method.
    """

    # References OBJECT PROXYING (PYTHON RECIPE) https://code.activestate.com/recipes/496741-object-proxying/

    __slots__ = [
        "__proxied",
    ]

    def __init__(self, name: "str", description: "str| None" = None):

        self.__proxied = get_provider(MaterialInterface)(
            name, description
        )  # type: ignore

    @staticmethod
    def get_preset(material_name: "PresetMaterial") -> "MaterialInterface":
        return get_provider(MaterialInterface).get_preset(material_name)

    def set_color(
        self,
        r_value: "int|float",
        g_value: "int|float",
        b_value: "int|float",
        a_value: "int|float" = 1.0,
    ) -> Self:
        return self.__proxied.set_color(r_value, g_value, b_value, a_value)

    def set_reflectivity(self, reflectivity: "float") -> Self:
        return self.__proxied.set_reflectivity(reflectivity)

    def set_roughness(self, roughness: "float") -> Self:
        return self.__proxied.set_roughness(roughness)

    def set_image_texture(self, image_file_path: "str") -> Self:
        return self.__proxied.set_image_texture(image_file_path)
