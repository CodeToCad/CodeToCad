# This file was forked from core/TestCodeToCADProvider.py

from typing import Optional
import unittest

from mock.modeling.MockModelingProvider import resetMockModelingProvider, injectMockModelingProvider

from CodeToCAD import *
import core.CodeToCADInterface as CodeToCADInterface
import core.utilities as Utilities
from core.utilities import (Angle, BoundaryBox, CurveTypes, Dimension,
                            Dimensions, Point, center, createUUIDLikeId,
                            getAbsoluteFilepath, getFilename, max, min)

if __name__ == "__main__":
    print("Started test_provider")

    import tests.test_providers
    unittest.main(tests.test_providers)

    print("Completed test_provider")


def injectMockProvider():
    resetMockModelingProvider()
    injectMockModelingProvider(globals())


class TestProviderCase(unittest.TestCase):

    def setUp(self) -> None:
        injectMockProvider()
        super().setUp()


class TestEntity(TestProviderCase):

    def test_isExists(self):
        instance = Part("name", "description").createCube(1, 1, 1)

        value = instance.isExists()

        assert value, "Get method failed."

    def test_rename(self):
        instance = Part("name", "description").createCube(1, 1, 1)

        value = instance.rename("newName", True)

        renamedPart = Part("newName")

        assert value.name == renamedPart.name, "Modify method failed."

        # TODO: test for renamelinkedEntitiesAndLandmarks = False. This is blocked by landmarking implementation

    def test_delete(self):
        instance = Part("name", "description").createCube(1, 1, 1)

        value = instance.isExists()

        assert value, "Expected True, got False"

        value = instance.delete(False)

        value = instance.isExists()

        assert not value, "Expected False, got True"

        # TODO: test for removeChildren = True

    def test_isVisible(self):
        instance = Part("name", "description").createCube(1, 1, 1)

        value = instance.isVisible()

        assert value, "Get method failed."

    def test_setVisible(self):
        instance = Part("name", "description").createCube(1, 1, 1)

        value = instance.setVisible(True)

        assert value.isVisible() == True, "Expected False, got True"

        value = instance.setVisible(False)

        assert value.isVisible() == False, "Expected True, got False"

    @unittest.skip("Blocked by understanding the consequences of implementating this capability.")
    def test_apply(self):
        instance = Part("name", "description")

        value = instance.apply()

        assert value, "Modify method failed."

    def test_getNativeInstance(self):
        instance = Part("name", "description").createCube(1, 1, 1)

        value = instance.getNativeInstance()

        assert value, "Get method failed."

    def test_getLocationWorld(self):
        instance = Part("name", "description").createCube(1, 1, 1)

        value = instance.getLocationWorld()

        assert value.x == 0 and value.y == 0 and value.z == 0, "Get method failed."

        # TODO: get location world after translating

    def test_getLocationLocal(self):
        instance = Part("name", "description").createCube(1, 1, 1)

        value = instance.getLocationWorld()

        assert value.x == 0 and value.y == 0 and value.z == 0, "Get method failed."

        # TODO: get location world after translating

    @unittest.skip("Not yet implemented")
    def test_select(self):
        instance = Part("name", "description")

        value = instance.select()

    def test_export(self):
        instance = Part("name", "description").createCube(1, 1, 1)

        value = instance.export("filePath.stl", True, 1.0)

        # no extension:
        self.assertRaises(
            AssertionError, lambda: instance.export("filePath", True, 1.0))

        # bad extension:
        self.assertRaises(
            AssertionError, lambda: instance.export("filePath.NotARealExtension", True, 1.0))

        # TODO: Test file absolute path resolution
        # TODO: Test export scale
        # TODO: Test overwriting

    def test_clone(self):
        instance = Part("name", "description").createCube(1, 1, 1)

        value = instance.clone("newName", False)

        assert instance.isExists(), "The original object should still exist."

        assert instance.name == value.name, "Clone should not return the cloned Entity."

        assert Part("newName").isExists(), "Clone method failed."

        # TODO: test copyLandmarks parameter

    def test_mirror(self):
        partToMirror = Part("partToMirror", "description").createCube(
            1, 1, 1).translateX(-5)
        partToMirrorAcross = Part(
            "partToMirrorAcross", "description").createCube(1, 1, 1)

        value = partToMirror.mirror(partToMirrorAcross, "x", None)

        assert value.isExists(), "Create method failed."

        # TODO: add test for bad mirrorAcrossEntity name
        # TODO: add test for bad axis name
        # TODO: add test for supplying resultingMirroredEntityName
        # TODO: add test to make sure mirrored object is really mirrored across the intended axis and distance

    def test_linearPattern(self):
        instance = Part("name", "description").createCube(1, 1, 1)

        value = instance.linearPattern(
            2, "2m")

        assert value.isExists(), "Modify method failed."

        # TODO: make sure patterning works on all axes correctly

    def test_circularPattern(self):
        partToPattern = Part(
            "partToPattern", "description").createCube(1, 1, 1).translateX(-5)
        centerPart = Part("centerPart", "description").createCube(1, 1, 1)

        value = partToPattern.circularPattern(
            4, 90, centerPart)

        assert value.isExists(), "Modify method failed."

        # TODO: make sure Entity, Landmark and string name all work correctly.
        # TODO: make sure patterning works on all axes correctly

    def test_translateXYZ(self):
        instance = Part("name", "description").createCube(1, 1, 1)

        value = instance.translateXYZ(5, 7, 9)

        assert value, "Modify method failed."

        assert instance.getLocationWorld() == Point(
            Dimension(5), Dimension(7), Dimension(9)), "Translation is not correct"

    def test_translateX(self):
        instance = Part("name", "description").createCube(1, 1, 1)

        value = instance.translateX(5)

        assert value, "Modify method failed."

        assert instance.getLocationWorld() == Point(
            Dimension(5), Dimension(0), Dimension(0)), "Translation is not correct"

    def test_translateY(self):
        instance = Part("name", "description").createCube(1, 1, 1)

        value = instance.translateY(5)

        assert value, "Modify method failed."

        assert instance.getLocationWorld() == Point(
            Dimension(0), Dimension(5), Dimension(0)), "Translation is not correct"

    def test_translateZ(self):
        instance = Part("name", "description").createCube(1, 1, 1)

        value = instance.translateZ(5)

        assert value, "Modify method failed."

        assert instance.getLocationWorld() == Point(
            Dimension(0), Dimension(0), Dimension(5)), "Translation is not correct"

    def test_scaleXYZ(self):
        instance = Part("name", "description").createCube(1, 1, 1)

        instance.scaleXYZ(5, 7, 9)

        dimensions = instance.getDimensions()

        assert dimensions.x.value == 5 and dimensions.y.value == 7 and dimensions.z.value == 9, "Modify method failed."

    def test_scaleX(self):
        instance = Part("name", "description").createCube(1, 1, 1)

        instance.scaleX(5)

        dimensions = instance.getDimensions()

        assert dimensions.x.value == 5 and dimensions.y.value == 1 and dimensions.z.value == 1, "Modify method failed."

    def test_scaleY(self):
        instance = Part("name", "description").createCube(1, 1, 1)

        instance.scaleY(5)

        dimensions = instance.getDimensions()

        assert dimensions.x.value == 1 and dimensions.y.value == 5 and dimensions.z.value == 1, "Modify method failed."

    def test_scaleZ(self):
        instance = Part("name", "description").createCube(1, 1, 1)

        instance.scaleZ(5)

        dimensions = instance.getDimensions()

        assert dimensions.x.value == 1 and dimensions.y.value == 1 and dimensions.z.value == 5, "Modify method failed."

    def test_scaleXByFactor(self):
        instance = Part("name", "description").createCube(1, 1, 1)

        instance.scaleXByFactor(5)

        dimensions = instance.getDimensions()

        assert dimensions.x.value == 5 and dimensions.y.value == 1 and dimensions.z.value == 1, "Modify method failed."

    def test_scaleYByFactor(self):
        instance = Part("name", "description").createCube(1, 1, 1)

        instance.scaleYByFactor(5)

        dimensions = instance.getDimensions()

        assert dimensions.x.value == 1 and dimensions.y.value == 5 and dimensions.z.value == 1, "Modify method failed."

    def test_scaleZByFactor(self):
        instance = Part("name", "description").createCube(1, 1, 1)

        instance.scaleZByFactor(5)

        dimensions = instance.getDimensions()

        assert dimensions.x.value == 1 and dimensions.y.value == 1 and dimensions.z.value == 5, "Modify method failed."

    def test_scaleKeepAspectRatio(self):
        instance = Part("name", "description").createCube(1, 1, 1)

        instance.scaleKeepAspectRatio(5, "x")

        dimensions = instance.getDimensions()

        assert dimensions.x.value == 5 and dimensions.y.value == 5 and dimensions.z.value == 5, "Modify method failed."

    def test_rotateXYZ(self):
        instance = Part("name", "description").createCube(1, 1, 1)

        value = instance.rotateXYZ(45, 45, 45)

        assert value, "Modify method failed."
        # TODO: check the rotation value

    def test_rotateX(self):
        instance = Part("name", "description").createCube(1, 1, 1)

        value = instance.rotateX(45)

        assert value, "Modify method failed."

    def test_rotateY(self):
        instance = Part("name", "description").createCube(1, 1, 1)

        value = instance.rotateY(45)

        assert value, "Modify method failed."

    def test_rotateZ(self):
        instance = Part("name", "description").createCube(1, 1, 1)

        value = instance.rotateZ(45)

        assert value, "Modify method failed."

    @unittest.skip
    def test_twist(self):
        instance = Part("name", "description")

        value = instance.twist("angle", "screwPitch", "interations", "axis")

        assert value, "Modify method failed."

    @unittest.skip
    def test_remesh(self):
        instance = Part("name", "description")

        value = instance.remesh("strategy", "amount")

        assert value, "Modify method failed."

    def test_createLandmark(self):
        instance = Part("name", "description").createCube(1, 1, 1)

        value = instance.createLandmark("landmarkName", 0, 0, 0)

        assert value, "Modify method failed."

        landmark = instance.getLandmark("landmarkName")

        assert landmark.isExists(), "Landmark was not created."

    def test_getBoundingBox(self):
        instance = Part("name", "description").createCube(1, 1, 1)

        value = instance.getBoundingBox()

        assert value, "Get method failed."
        assert value.x.center == 0.0
        assert value.y.center == 0.0
        assert value.z.center == 0.0
        assert value.x.min == -0.5
        assert value.x.max == 0.5
        assert value.y.min == -0.5
        assert value.y.max == 0.5
        assert value.z.min == -0.5
        assert value.z.max == 0.5

    def test_getDimensions(self):
        instance = Part("name", "description").createCube(1, 1, 1)

        value = instance.getDimensions()

        assert value, "Get method failed."
        assert value.height == 1
        assert value.width == 1
        assert value.length == 1

    def test_getLandmark(self):
        instance = Part("name", "description").createCube(1, 1, 1)
        instance.createLandmark("landmarkName", max, max, max)

        value = instance.getLandmark("landmarkName")

        valueLocation = value.getLocationWorld()

        assert value, "Get method failed."
        assert valueLocation.x == 0.5
        assert valueLocation.y == 0.5
        assert valueLocation.z == 0.5


class TestPart(TestProviderCase):

    @unittest.skip
    def test_createFromFile(self):
        instance = Part("TestPart")

        import pathlib

        value = instance.createFromFile(
            f"{pathlib.Path(__file__).parent}/../examples/importableCube.stl")

        assert value.isExists(), "Create method failed."

    def test_createCube(self):
        instance = Part("TestPart")

        value = instance.createCube(
            1, 1, 1)

        assert value.isExists(), "Create method failed."

    @unittest.skip
    def test_createCone(self):
        instance = Part("TestPart")

        value = instance.createCone(
            1, 1, 1)

        assert value.isExists(), "Create method failed."

    @unittest.skip
    def test_createCylinder(self):
        instance = Part("TestPart")

        value = instance.createCylinder(1, 1)

        assert value.isExists(), "Create method failed."

    @unittest.skip
    def test_createTorus(self):
        instance = Part("TestPart")

        value = instance.createTorus(
            0.5, 1)

        assert value.isExists(), "Create method failed."

    @unittest.skip
    def test_createSphere(self):
        instance = Part("TestPart")

        value = instance.createSphere(1)

        assert value.isExists(), "Create method failed."

    @unittest.skip
    def test_createGear(self):
        instance = Part("TestPart")

        value = instance.createGear(1, 1, 1, 1, 1)

        assert value.isExists(), "Create method failed."

    @unittest.skip
    def test_loft(self):
        instance = Part("TestPart")

        value = instance.loft("Landmark1", "Landmark2")

        assert value.isExists(), "Create method failed."

    @unittest.skip
    def test_union(self):
        instance = Part("TestPart")

        value = instance.union(
            "withPart", "deleteAfterUnion", "isTransferLandmarks")

        assert value, "Modify method failed."

    @unittest.skip
    def test_subtract(self):
        instance = Part("TestPart")

        value = instance.subtract(
            "withPart", "deleteAfterSubtract", "isTransferLandmarks")

        assert value, "Modify method failed."

    @unittest.skip
    def test_intersect(self):
        instance = Part("TestPart")

        value = instance.intersect(
            "withPart", "deleteAfterIntersect", "isTransferLandmarks")

        assert value, "Modify method failed."

    @unittest.skip
    def test_hollow(self):
        instance = Part("TestPart")

        value = instance.hollow(
            "thicknessX", "thicknessY", "thicknessZ", "startAxis", "flipAxis")

        assert value, "Modify method failed."

    @unittest.skip
    def test_hole(self):
        instance = Part("TestPart")

        value = instance.hole("holeLandmark", "radius", "depth", "normalAxis", False, "initialRotationX", "initialRotationY", "initialRotationZ", "mirrorAboutEntityOrLandmark", "mirrorAxis", False, 1,
                              "circularPatternInstanceSeparation", "circularPatternInstanceAxis", "circularPatternAboutEntityOrLandmark", 1, "linearPatternInstanceSeparation", "linearPatternInstanceAxis")

        assert value, "Modify method failed."

    def test_assignMaterial(self):
        instance = Part("TestPart").createCube(1, 1, 1)

        value = instance.assignMaterial("materialName")

        assert value, "Modify method failed."

    @unittest.skip
    def test_isCollidingWithPart(self):
        instance = Part("TestPart")

        value = instance.isCollidingWithPart("otherPart")

        assert value, "Get method failed."

    @unittest.skip
    def test_filletAllEdges(self):
        instance = Part("TestPart")

        value = instance.filletAllEdges("radius", "useWidth")

        assert value, "Modify method failed."

    @unittest.skip
    def test_filletEdges(self):
        instance = Part("TestPart")

        value = instance.filletEdges(
            "radius", "landmarksNearEdges", "useWidth")

        assert value, "Modify method failed."

    @unittest.skip
    def test_filletFaces(self):
        instance = Part("TestPart")

        value = instance.filletFaces(
            "radius", "landmarksNearFaces", "useWidth")

        assert value, "Modify method failed."

    @unittest.skip
    def test_chamferAllEdges(self):
        instance = Part("TestPart")

        value = instance.chamferAllEdges("radius")

        assert value, "Modify method failed."

    @unittest.skip
    def test_chamferEdges(self):
        instance = Part("TestPart")

        value = instance.chamferEdges("radius", "landmarksNearEdges")

        assert value, "Modify method failed."

    @unittest.skip
    def test_chamferFaces(self):
        instance = Part("TestPart")

        value = instance.chamferFaces("radius", "landmarksNearFaces")

        assert value, "Modify method failed."

    @unittest.skip
    def test_selectVertexNearLandmark(self):
        instance = Part("TestPart")

        value = instance.selectVertexNearLandmark("landmarkName")

    @unittest.skip
    def test_selectEdgeNearLandmark(self):
        instance = Part("TestPart")

        value = instance.selectEdgeNearLandmark("landmarkName")

    @unittest.skip
    def test_selectFaceNearLandmark(self):
        instance = Part("TestPart")

        value = instance.selectFaceNearLandmark("landmarkName")


class TestSketch(TestProviderCase):

    @unittest.skip
    def test_revolve(self):
        instance = Sketch("name", "curveType", "description")

        value = instance.revolve("angle", "aboutEntityOrLandmark", "axis")

        assert value, "Modify method failed."

    @unittest.skip
    def test_extrude(self):
        instance = Sketch("name", "curveType", "description")

        value = instance.extrude("length", "convertToMesh")

        assert value, "Modify method failed."

    @unittest.skip
    def test_sweep(self):
        instance = Sketch("name", "curveType", "description")

        value = instance.sweep("profileCurveName", "fillCap")

        assert value, "Modify method failed."

    @unittest.skip
    def test_createText(self):
        instance = Sketch("name", "curveType", "description")

        value = instance.createText("text", "fontSize", "bold", "italic", "underlined",
                                    "characterSpacing", "wordSpacing", "lineSpacing", "fontFilePath")

        assert value.isExists(), "Create method failed."

    @unittest.skip
    def test_createFromVertices(self):
        instance = Sketch("name", "curveType", "description")

        value = instance.createFromVertices("coordinates", "interpolation")

        assert value.isExists(), "Create method failed."

    @unittest.skip
    def test_createPoint(self):
        instance = Sketch("name", "curveType", "description")

        value = instance.createPoint("coordinate")

        assert value.isExists(), "Create method failed."

    @unittest.skip
    def test_createLine(self):
        instance = Sketch("name", "curveType", "description")

        value = instance.createLine("length", "angleX", "angleY", "symmetric")

        assert value.isExists(), "Create method failed."

    @unittest.skip
    def test_createLineBetweenPoints(self):
        instance = Sketch("name", "curveType", "description")

        value = instance.createLineBetweenPoints("endAt", "startAt")

        assert value.isExists(), "Create method failed."

    @unittest.skip
    def test_createCircle(self):
        instance = Sketch("name", "curveType", "description")

        value = instance.createCircle("radius")

        assert value.isExists(), "Create method failed."

    @unittest.skip
    def test_createEllipse(self):
        instance = Sketch("name", "curveType", "description")

        value = instance.createEllipse("radiusA", "radiusB")

        assert value.isExists(), "Create method failed."

    @unittest.skip
    def test_createArc(self):
        instance = Sketch("name", "curveType", "description")

        value = instance.createArc("radius", "angle")

        assert value.isExists(), "Create method failed."

    @unittest.skip
    def test_createArcBetweenThreePoints(self):
        instance = Sketch("name", "curveType", "description")

        value = instance.createArcBetweenThreePoints(
            "pointA", "pointB", "centerPoint")

        assert value.isExists(), "Create method failed."

    @unittest.skip
    def test_createSegment(self):
        instance = Sketch("name", "curveType", "description")

        value = instance.createSegment("innerRadius", "outerRadius", "angle")

        assert value.isExists(), "Create method failed."

    @unittest.skip
    def test_createRectangle(self):
        instance = Sketch("name", "curveType", "description")

        value = instance.createRectangle("length", "width")

        assert value.isExists(), "Create method failed."

    @unittest.skip
    def test_createPolygon(self):
        instance = Sketch("name", "curveType", "description")

        value = instance.createPolygon("numberOfSides", "length", "width")

        assert value.isExists(), "Create method failed."

    @unittest.skip
    def test_createTrapezoid(self):
        instance = Sketch("name", "curveType", "description")

        value = instance.createTrapezoid(
            "lengthUpper", "lengthLower", "height")

        assert value.isExists(), "Create method failed."


class TestLandmark(TestProviderCase):

    @unittest.skip
    def test_getLandmarkEntityName(self):
        instance = Landmark("name", "parentEntity", "description")

        value = instance.getLandmarkEntityName("")

        assert value, "Get method failed."

    @unittest.skip
    def test_getParentEntity(self):
        instance = Landmark("name", "parentEntity", "description")

        value = instance.getParentEntity("")

        assert value, "Get method failed."

    @unittest.skip
    def test_isExists(self):
        instance = Landmark("name", "parentEntity", "description")

        value = instance.isExists("")

        assert value, "Get method failed."

    @unittest.skip
    def test_rename(self):
        instance = Landmark("name", "parentEntity", "description")

        value = instance.rename("newName", "renamelinkedEntitiesAndLandmarks")

        assert value, "Modify method failed."

    @unittest.skip
    def test_delete(self):
        instance = Landmark("name", "parentEntity", "description")

        value = instance.delete("removeChildren")

    @unittest.skip
    def test_isVisible(self):
        instance = Landmark("name", "parentEntity", "description")

        value = instance.isVisible("")

        assert value, "Get method failed."

    @unittest.skip
    def test_setVisible(self):
        instance = Landmark("name", "parentEntity", "description")

        value = instance.setVisible("isVisible")

    @unittest.skip
    def test_getNativeInstance(self):
        instance = Landmark("name", "parentEntity", "description")

        value = instance.getNativeInstance("")

        assert value, "Get method failed."

    @unittest.skip
    def test_getLocationWorld(self):
        instance = Landmark("name", "parentEntity", "description")

        value = instance.getLocationWorld("")

        assert value, "Get method failed."

    @unittest.skip
    def test_getLocationLocal(self):
        instance = Landmark("name", "parentEntity", "description")

        value = instance.getLocationLocal("")

        assert value, "Get method failed."

    @unittest.skip
    def test_select(self):
        instance = Landmark("name", "parentEntity", "description")

        value = instance.select("landmarkName", "selectionType")


class TestJoint(TestProviderCase):

    @unittest.skip
    def test_translateLandmarkOntoAnother(self):
        instance = Joint("entity1", "entity2")

        value = instance.translateLandmarkOntoAnother("")

        assert value, "Modify method failed."

    @unittest.skip
    def test_pivot(self):
        instance = Joint("entity1", "entity2")

        value = instance.pivot("")

        assert value, "Modify method failed."

    @unittest.skip
    def test_gearRatio(self):
        instance = Joint("entity1", "entity2")

        value = instance.gearRatio("ratio")

        assert value, "Modify method failed."

    @unittest.skip
    def test_limitLocationX(self):
        instance = Joint("entity1", "entity2")

        value = instance.limitLocationX("min", "max")

        assert value, "Modify method failed."

    @unittest.skip
    def test_limitLocationY(self):
        instance = Joint("entity1", "entity2")

        value = instance.limitLocationY("min", "max")

        assert value, "Modify method failed."

    @unittest.skip
    def test_limitLocationZ(self):
        instance = Joint("entity1", "entity2")

        value = instance.limitLocationZ("min", "max")

        assert value, "Modify method failed."

    @unittest.skip
    def test_limitRotationX(self):
        instance = Joint("entity1", "entity2")

        value = instance.limitRotationX("min", "max")

        assert value, "Modify method failed."

    @unittest.skip
    def test_limitRotationY(self):
        instance = Joint("entity1", "entity2")

        value = instance.limitRotationY("min", "max")

        assert value, "Modify method failed."

    @unittest.skip
    def test_limitRotationZ(self):
        instance = Joint("entity1", "entity2")

        value = instance.limitRotationZ("min", "max")

        assert value, "Modify method failed."


class TestMaterial(TestProviderCase):

    @unittest.skip
    def test_assignToPart(self):
        instance = Material("name", "description")

        value = instance.assignToPart("partName")

        assert value, "Modify method failed."

    @unittest.skip
    def test_setColor(self):
        instance = Material("name", "description")

        value = instance.setColor("rValue", "gValue", "bValue", "aValue")

        assert value, "Modify method failed."

    @unittest.skip
    def test_addImageTexture(self):
        instance = Material("name", "description")

        value = instance.addImageTexture("imageFilePath")

        assert value, "Modify method failed."


class TestAnimation(TestProviderCase):

    @unittest.skip
    def test_createKeyFrameLocation(self):
        instance = Animation("")

        value = instance.createKeyFrameLocation("entity", "frameNumber")

    @unittest.skip
    def test_createKeyFrameRotation(self):
        instance = Animation("")

        value = instance.createKeyFrameRotation("entity", "frameNumber")


class TestScene(TestProviderCase):

    @unittest.skip
    def test_create(self):
        instance = Scene("name", "description")

        value = instance.create("")

        assert value.isExists(), "Create method failed."

    @unittest.skip
    def test_delete(self):
        instance = Scene("name", "description")

        value = instance.delete("")

    @unittest.skip
    def test_export(self):
        instance = Scene("name", "description")

        value = instance.export("filePath", "entities", "overwrite", "scale")

    @unittest.skip
    def test_setDefaultUnit(self):
        instance = Scene("name", "description")

        value = instance.setDefaultUnit("unit")

    @unittest.skip
    def test_createGroup(self):
        instance = Scene("name", "description")

        value = instance.createGroup("name")

        assert value.isExists(), "Create method failed."

    @unittest.skip
    def test_deleteGroup(self):
        instance = Scene("name", "description")

        value = instance.deleteGroup("name", "removeChildren")

    @unittest.skip
    def test_removeFromGroup(self):
        instance = Scene("name", "description")

        value = instance.removeFromGroup("entityName", "groupName")

    @unittest.skip
    def test_assignToGroup(self):
        instance = Scene("name", "description")

        value = instance.assignToGroup(
            "entities", "groupName", "removeFromOtherGroups")

    @unittest.skip
    def test_setVisible(self):
        instance = Scene("name", "description")

        value = instance.setVisible("entities", "isVisible")


class TestAnalytics(TestProviderCase):

    @unittest.skip
    def test_measureDistance(self):
        instance = Analytics("")

        value = instance.measureDistance("entity1", "entity2")

        assert value, "Get method failed."

    @unittest.skip
    def test_measureAngle(self):
        instance = Analytics("")

        value = instance.measureAngle("entity1", "entity2", "pivot")

        assert value, "Get method failed."

    @unittest.skip
    def test_getWorldPose(self):
        instance = Analytics("")

        value = instance.getWorldPose("entity")

        assert value, "Get method failed."

    @unittest.skip
    def test_getBoundingBox(self):
        instance = Analytics("")

        value = instance.getBoundingBox("entityName")

        assert value, "Get method failed."

    @unittest.skip
    def test_getDimensions(self):
        instance = Analytics("")

        value = instance.getDimensions("entityName")

        assert value, "Get method failed."
