import abc
from abc import ABC
from typing import Type, Set, Optional

from svgwrite.base import BaseElement
from svgwrite.container import Marker

from src.utils.config import Config

config = Config()


class Glyph(ABC):
    """
    Glyph
    """

    def __init__(self, class_name: str):
        """
        Constructor
        :param class_name: name of the class
        :type class_name: str
        """
        self.class_name = class_name

    @classmethod
    def start_marker(cls) -> Optional[Marker]:
        return None

    @classmethod
    def end_marker(cls) -> Optional[Marker]:
        return None

    @classmethod
    def symbol(cls) -> Optional[Marker]:
        return None

    # pylint: disable=no-self-use
    def draw(self) -> Optional[BaseElement]:
        return None

    @property
    def priority(self) -> int:
        return 1

    def __lt__(self, other: 'Glyph') -> bool:
        return self.priority < other.priority

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.class_name}')"

    @property
    def used_classes(self) -> Set[Type['Glyph']]:
        return set(self.__class__.__mro__).difference({abc.ABC, object})
