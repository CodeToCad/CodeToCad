# THIS IS AN AUTO-GENERATE FILE.
# DO NOT EDIT MANUALLY.
# Please run development/capabilities_json_to_python/capabilities_to_py.sh to generate this file.

from abc import ABCMeta, abstractmethod


from codetocad.codetocad_types import *
from codetocad.utilities import *
from codetocad.core import *
from codetocad.enums import *


class BooleanableInterface(metaclass=ABCMeta):

    """
    An entity that supports boolean operations: union, intersect, subtract.
    """

    @abstractmethod
    def union(
        self,
        other: "BooleanableOrItsName",
        delete_after_union: "bool" = True,
        is_transfer_data: "bool" = False,
    ):
        """
        Boolean union
        """

        print("union is called in an abstract method. Please override this method.")

        raise NotImplementedError()

    @abstractmethod
    def subtract(
        self,
        other: "BooleanableOrItsName",
        delete_after_subtract: "bool" = True,
        is_transfer_data: "bool" = False,
    ):
        """
        Boolean subtraction
        """

        print("subtract is called in an abstract method. Please override this method.")

        raise NotImplementedError()

    @abstractmethod
    def intersect(
        self,
        other: "BooleanableOrItsName",
        delete_after_intersect: "bool" = True,
        is_transfer_data: "bool" = False,
    ):
        """
        Boolean intersection
        """

        print("intersect is called in an abstract method. Please override this method.")

        raise NotImplementedError()