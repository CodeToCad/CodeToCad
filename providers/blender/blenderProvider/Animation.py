

from typing import Optional

from . import BlenderActions
from . import BlenderDefinitions

from codetocad.interfaces import AnimationInterface
from codetocad.CodeToCADTypes import *
from codetocad.utilities import *


class Animation(AnimationInterface):

    def __init__(self):
        pass

    @staticmethod
    def default(
    ) -> 'Animation':
        return Animation()

    def setFrameStart(self, frameNumber: 'int'
                      ):

        BlenderActions.setFrameStart(frameNumber, None)

        return self

    def setFrameEnd(self, frameNumber: 'int'
                    ):

        BlenderActions.setFrameEnd(frameNumber, None)

        return self

    def setFrameCurrent(self, frameNumber: 'int'
                        ):

        BlenderActions.setFrameCurrent(frameNumber, None)

        return self

    def createKeyFrameLocation(self, entity: EntityOrItsName, frameNumber: 'int'
                               ):
        partName = entity

        if isinstance(partName, EntityInterface):
            partName = partName.name

        BlenderActions.addKeyframeToObject(
            partName, frameNumber, BlenderDefinitions.BlenderTranslationTypes.ABSOLUTE.value)

        return self

    def createKeyFrameRotation(self, entity: EntityOrItsName, frameNumber: 'int'
                               ):
        partName = entity

        if isinstance(partName, EntityInterface):
            partName = partName.name

        BlenderActions.addKeyframeToObject(
            partName, frameNumber, BlenderDefinitions.BlenderRotationTypes.EULER.value)

        return self
