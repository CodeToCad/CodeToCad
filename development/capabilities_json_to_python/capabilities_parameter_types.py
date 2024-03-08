"""
Type-mapping, hand-crafted for templating purposes.
"""


def capabilities_type_to_python_type(type_name: str):
    return capabilities_parameter_types.get(type_name, type_name)


capabilities_parameter_types = {
    "string": "str",
    "array": "list",
    "object": "dict",
    "any": "object",
    "number": "int",
    "float": "float",
    "boolean": "bool",
    "string,float": "FloatOrItsStringValue",
    "int,float": "IntOrFloat",
    "string,Part": "PartOrItsName",
    "string,Entity": "EntityOrItsName",
    "string,Sketch": "SketchOrItsName",
    "list[string,Entity]": "list[EntityOrItsName]",
    "string,Landmark": "LandmarkOrItsName",
    "list[string,Landmark]": "list[LandmarkOrItsName]",
    "string,Material": "MaterialOrItsName",
    "string,int,Axis": "AxisOrItsIndexOrItsName",
    "string,float,Dimension": "DimensionOrItsFloatOrStringValue",
    "string,list[string],list[float],list[Dimension],Dimensions": "DimensionsOrItsListOfFloatOrString",
    "string,float,Angle": "AngleOrItsFloatOrStringValue",
    "string,Entity": "EntityOrItsName",
    "string,list[string],list[float],list[Dimension],Point": "PointOrListOfFloatOrItsStringValue",
    "list[string,list[string],list[float],list[Dimension],Point]": "list[PointOrListOfFloatOrItsStringValue]",
    "string,list[string],list[float],list[Dimension],Point,Vertex": "PointOrListOfFloatOrItsStringValueOrVertex",
    "list[string,list[string],list[float],list[Dimension],Point,Vertex]": "list[PointOrListOfFloatOrItsStringValueOrVertex]",
    "string,LengthUnit": "LengthUnitOrItsName",
    "string,PresetLandmark": "PresetLandmarkOrItsName",
    "string,Camera": "CameraOrItsName",
    "string,Exportable": "ExportableOrItsName",
    "list[string,Exportable]": "list[ExportableOrItsName]",
    "string,Booleanable": "BooleanableOrItsName",
    "string,Landmarkable": "LandmarkableOrItsName",
}
