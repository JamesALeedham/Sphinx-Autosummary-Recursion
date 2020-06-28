"""
Module containing a class, global function, exception, type variable and type alias.

For some reason, the type variable is included in the list of variables and so is automatically
summarised and documented, but the type alias isn't.

The type alias can be documented manually using the `autodata` directive::

    .. autodata:: myTypeAlias

.. autodata:: myTypeAlias
"""
from typing import List, Tuple, Union, TypeVar

myTypeAlias = Union[List[str], Tuple[int, int]]
"""This is a type alias."""

myTypeVar = TypeVar("T", bound=int)
"""This is a type variable."""


class myClass1:
    """
    This is a base class.
    """
    def __init__(self, arg1: myTypeAlias, arg2: str):
        """
        :param arg1: Pass a :data:`~mytoolbox.mymodule1.myTypeAlias` in first.
        :param arg2: Pass a string in second.
        """
        self.arg = arg1

    def __call__(self, arg: int) -> str:
        """
        This class is callable.

        :param arg: Pass one of these in.
        :return: Get one of these out.
        """

    def myMethod1(self, arg: myTypeVar) -> str:
        """
        This is the first public method.

        :param arg: Pass a :data:`~mytoolbox.mymodule1.myTypeVar` in.
        :return: Get one of these out.
        """
        pass

    def myMethod2(self) -> str:
        """This is the second public method."""
        pass

    @property
    def myAttribute(self) -> int:
        """This is a public attribute."""
        pass

    def _myPrivateMethod(self):
        """This is a private method, so this docstring shouldn't be visible."""
        pass

def myGlobalFunction(arg1: str, arg2: bool) -> bool:
  """
  This is a global function.

  :param arg1: Pass this in first.
  :param arg2: Pass this in second.
  :return: Whether to go (`True`) or not go (`False`).
  """
  pass


class myError(Exception):
    """
    This is a custom error.
    """
    pass
