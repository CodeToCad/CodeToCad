# THIS IS AN AUTO-GENERATE FILE.
# DO NOT EDIT MANUALLY.
# Please run development/capabilities_json_to_python/capabilities_to_py.sh to generate this file.

from abc import ABCMeta, abstractmethod


from codetocad.codetocad_types import *

from typing import Self


# Implementable dependencies:


# Interface dependencies:


# Extended dependencies:


class ScalableInterface(metaclass=ABCMeta):
    """
    An entity that can be transformed by a scale.
    """

    @abstractmethod
    def scale_xyz(
        self,
        x: "str|float|Dimension",
        y: "str|float|Dimension",
        z: "str|float|Dimension",
    ) -> Self:
        """
        Scale in the XYZ directions. Pass a number, Dimension or Dimension-String (e.g. '2cm') to scale to a specific length.
        """

        print("scale_xyz is called in an abstract method. Please override this method.")

        raise NotImplementedError()

    @abstractmethod
    def scale_x(self, scale: "str|float|Dimension") -> Self:
        """
        Scale in the X direction. Pass a number, Dimension or Dimension-String (e.g. '2cm') to scale to a specific length.
        """

        print("scale_x is called in an abstract method. Please override this method.")

        raise NotImplementedError()

    @abstractmethod
    def scale_y(self, scale: "str|float|Dimension") -> Self:
        """
        Scale in the Y direction. Pass a number, Dimension or Dimension-String (e.g. '2cm') to scale to a specific length.
        """

        print("scale_y is called in an abstract method. Please override this method.")

        raise NotImplementedError()

    @abstractmethod
    def scale_z(self, scale: "str|float|Dimension") -> Self:
        """
        Scale in the Z direction. Pass a number, Dimension or Dimension-String (e.g. '2cm') to scale to a specific length.
        """

        print("scale_z is called in an abstract method. Please override this method.")

        raise NotImplementedError()

    @abstractmethod
    def scale_x_by_factor(self, scale_factor: "float") -> Self:
        """
        Scale in the X direction by a multiple.
        """

        print(
            "scale_x_by_factor is called in an abstract method. Please override this method."
        )

        raise NotImplementedError()

    @abstractmethod
    def scale_y_by_factor(self, scale_factor: "float") -> Self:
        """
        Scale in the Y direction by a multiple.
        """

        print(
            "scale_y_by_factor is called in an abstract method. Please override this method."
        )

        raise NotImplementedError()

    @abstractmethod
    def scale_z_by_factor(self, scale_factor: "float") -> Self:
        """
        Scale in the X direction by a multiple.
        """

        print(
            "scale_z_by_factor is called in an abstract method. Please override this method."
        )

        raise NotImplementedError()

    @abstractmethod
    def scale_keep_aspect_ratio(
        self, scale: "str|float|Dimension", axis: "str|int|Axis"
    ) -> Self:
        """
        Scale in one axis and maintain the others. Pass a Dimension or Dimension-String (e.g. '2cm') to scale to a specific length.
        """

        print(
            "scale_keep_aspect_ratio is called in an abstract method. Please override this method."
        )

        raise NotImplementedError()
