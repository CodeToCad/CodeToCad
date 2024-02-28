# THIS IS AN AUTO-GENERATE FILE.
# DO NOT EDIT MANUALLY.
# Please run development/capabilities_json_to_python/capabilities_to_py.sh to generate this file.

# testsSample will implement these interfaces - this ensures that as capabilities.json is updated, tests are up to date as well.
from unittest import skip

from .test_helper import *
from codetocad.tests_interfaces import WireTestInterface


from codetocad import Landmark, Vertex, Wire, Part, Entity, Edge


class WireTest(TestProviderCase, WireTestInterface):
    @skip("TODO")
    def test_get_normal(self):
        instance = Wire(
            name="String",
            edges=[
                Edge(
                    v1=Vertex(
                        "a vertex", Point.from_list_of_float_or_string([0, 0, 0])
                    ),
                    v2=Vertex(
                        "a vertex", Point.from_list_of_float_or_string([0, 0, 0])
                    ),
                    name="an edge",
                )
            ],
            description="String",
            native_instance=value,
            parent_entity=__import__("codetocad").Part("an entity"),
        )

        value = instance.get_normal(flip=False)

        assert value, "Get method failed."

    @skip("TODO")
    def test_get_vertices(self):
        instance = Wire(
            name="String",
            edges=[
                Edge(
                    v1=Vertex(
                        "a vertex", Point.from_list_of_float_or_string([0, 0, 0])
                    ),
                    v2=Vertex(
                        "a vertex", Point.from_list_of_float_or_string([0, 0, 0])
                    ),
                    name="an edge",
                )
            ],
            description="String",
            native_instance=value,
            parent_entity=__import__("codetocad").Part("an entity"),
        )

        value = instance.get_vertices()

        assert value, "Get method failed."

    @skip("TODO")
    def test_get_is_closed(self):
        instance = Wire(
            name="String",
            edges=[
                Edge(
                    v1=Vertex(
                        "a vertex", Point.from_list_of_float_or_string([0, 0, 0])
                    ),
                    v2=Vertex(
                        "a vertex", Point.from_list_of_float_or_string([0, 0, 0])
                    ),
                    name="an edge",
                )
            ],
            description="String",
            native_instance=value,
            parent_entity=__import__("codetocad").Part("an entity"),
        )

        value = instance.get_is_closed()

        assert value, "Get method failed."

    @skip("TODO")
    def test_loft(self):
        instance = Wire(
            name="String",
            edges=[
                Edge(
                    v1=Vertex(
                        "a vertex", Point.from_list_of_float_or_string([0, 0, 0])
                    ),
                    v2=Vertex(
                        "a vertex", Point.from_list_of_float_or_string([0, 0, 0])
                    ),
                    name="an edge",
                )
            ],
            description="String",
            native_instance=value,
            parent_entity=__import__("codetocad").Part("an entity"),
        )

        value = instance.loft(
            other=Wire(
                "a wire",
                [
                    Edge(
                        v1=Vertex(
                            "a vertex", Point.from_list_of_float_or_string([0, 0, 0])
                        ),
                        v2=Vertex(
                            "a vertex", Point.from_list_of_float_or_string([0, 0, 0])
                        ),
                        name="an edge",
                    )
                ],
            ),
            new_part_name="String",
        )

        assert value, "Get method failed."

    @skip("TODO")
    def test_mirror(self):
        instance = Wire(
            name="String",
            edges=[
                Edge(
                    v1=Vertex(
                        "a vertex", Point.from_list_of_float_or_string([0, 0, 0])
                    ),
                    v2=Vertex(
                        "a vertex", Point.from_list_of_float_or_string([0, 0, 0])
                    ),
                    name="an edge",
                )
            ],
            description="String",
            native_instance=value,
            parent_entity=__import__("codetocad").Part("an entity"),
        )

        value = instance.mirror(
            mirror_across_entity=__import__("codetocad").Part("an entity"),
            axis=x,
            resulting_mirrored_entity_name="String",
        )

        assert value.is_exists(), "Create method failed."

    @skip("TODO")
    def test_linear_pattern(self):
        instance = Wire(
            name="String",
            edges=[
                Edge(
                    v1=Vertex(
                        "a vertex", Point.from_list_of_float_or_string([0, 0, 0])
                    ),
                    v2=Vertex(
                        "a vertex", Point.from_list_of_float_or_string([0, 0, 0])
                    ),
                    name="an edge",
                )
            ],
            description="String",
            native_instance=value,
            parent_entity=__import__("codetocad").Part("an entity"),
        )

        value = instance.linear_pattern(
            instance_count=0, offset=Dimension(0, "mm"), direction_axis="z"
        )

        assert value, "Modify method failed."

    @skip("TODO")
    def test_circular_pattern(self):
        instance = Wire(
            name="String",
            edges=[
                Edge(
                    v1=Vertex(
                        "a vertex", Point.from_list_of_float_or_string([0, 0, 0])
                    ),
                    v2=Vertex(
                        "a vertex", Point.from_list_of_float_or_string([0, 0, 0])
                    ),
                    name="an edge",
                )
            ],
            description="String",
            native_instance=value,
            parent_entity=__import__("codetocad").Part("an entity"),
        )

        value = instance.circular_pattern(
            instance_count=0,
            separation_angle=Angle("90"),
            center_entity_or_landmark=__import__("codetocad").Part("an entity"),
            normal_direction_axis="z",
        )

        assert value, "Modify method failed."

    @skip("TODO")
    def test_project(self):
        instance = Wire(
            name="String",
            edges=[
                Edge(
                    v1=Vertex(
                        "a vertex", Point.from_list_of_float_or_string([0, 0, 0])
                    ),
                    v2=Vertex(
                        "a vertex", Point.from_list_of_float_or_string([0, 0, 0])
                    ),
                    name="an edge",
                )
            ],
            description="String",
            native_instance=value,
            parent_entity=__import__("codetocad").Part("an entity"),
        )

        value = instance.project(
            project_from=__import__("codetocad").Sketch("a projected sketch")
        )

        assert value, "Get method failed."

    @skip("TODO")
    def test_create_landmark(self):
        instance = Wire(
            name="String",
            edges=[
                Edge(
                    v1=Vertex(
                        "a vertex", Point.from_list_of_float_or_string([0, 0, 0])
                    ),
                    v2=Vertex(
                        "a vertex", Point.from_list_of_float_or_string([0, 0, 0])
                    ),
                    name="an edge",
                )
            ],
            description="String",
            native_instance=value,
            parent_entity=__import__("codetocad").Part("an entity"),
        )

        value = instance.create_landmark(
            landmark_name="String",
            x=Dimension(0, "mm"),
            y=Dimension(0, "mm"),
            z=Dimension(0, "mm"),
        )

        assert value, "Get method failed."

    @skip("TODO")
    def test_get_landmark(self):
        instance = Wire(
            name="String",
            edges=[
                Edge(
                    v1=Vertex(
                        "a vertex", Point.from_list_of_float_or_string([0, 0, 0])
                    ),
                    v2=Vertex(
                        "a vertex", Point.from_list_of_float_or_string([0, 0, 0])
                    ),
                    name="an edge",
                )
            ],
            description="String",
            native_instance=value,
            parent_entity=__import__("codetocad").Part("an entity"),
        )

        value = instance.get_landmark(landmark_name=PresetLandmark.topLeft)

        assert value, "Get method failed."

    @skip("TODO")
    def test_union(self):
        instance = Wire(
            name="String",
            edges=[
                Edge(
                    v1=Vertex(
                        "a vertex", Point.from_list_of_float_or_string([0, 0, 0])
                    ),
                    v2=Vertex(
                        "a vertex", Point.from_list_of_float_or_string([0, 0, 0])
                    ),
                    name="an edge",
                )
            ],
            description="String",
            native_instance=value,
            parent_entity=__import__("codetocad").Part("an entity"),
        )

        value = instance.union(
            other=__import__("codetocad").Part("a booleanable part"),
            delete_after_union=True,
            is_transfer_data=False,
        )

        assert value, "Modify method failed."

    @skip("TODO")
    def test_subtract(self):
        instance = Wire(
            name="String",
            edges=[
                Edge(
                    v1=Vertex(
                        "a vertex", Point.from_list_of_float_or_string([0, 0, 0])
                    ),
                    v2=Vertex(
                        "a vertex", Point.from_list_of_float_or_string([0, 0, 0])
                    ),
                    name="an edge",
                )
            ],
            description="String",
            native_instance=value,
            parent_entity=__import__("codetocad").Part("an entity"),
        )

        value = instance.subtract(
            other=__import__("codetocad").Part("a booleanable part"),
            delete_after_subtract=True,
            is_transfer_data=False,
        )

        assert value, "Modify method failed."

    @skip("TODO")
    def test_intersect(self):
        instance = Wire(
            name="String",
            edges=[
                Edge(
                    v1=Vertex(
                        "a vertex", Point.from_list_of_float_or_string([0, 0, 0])
                    ),
                    v2=Vertex(
                        "a vertex", Point.from_list_of_float_or_string([0, 0, 0])
                    ),
                    name="an edge",
                )
            ],
            description="String",
            native_instance=value,
            parent_entity=__import__("codetocad").Part("an entity"),
        )

        value = instance.intersect(
            other=__import__("codetocad").Part("a booleanable part"),
            delete_after_intersect=True,
            is_transfer_data=False,
        )

        assert value, "Modify method failed."
