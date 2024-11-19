"""Glyph."""
import abc
from typing import Type

from svgwrite.base import BaseElement
from svgwrite.container import Marker

from src.utils.config import Config

config = Config()


class Glyph:
    """Base class for defining a glyph, with support for SVG markers and drawing functionality."""

    def __init__(self, class_name: str):
        """Initialize the Glyph with a class name that defines its styling in CSS.

        Args:
            class_name (str): The class name for the SVG element, which is used for styling.
                               Different classes can create the same glyph with different styles.
        """
        self.class_name = class_name

    @classmethod
    def start_marker(cls) -> Marker | None:
        """Return the starting marker for the glyph.

        Returns:
            Marker | None: The start marker element, or None if not applicable.
        """
        return None

    @classmethod
    def end_marker(cls) -> Marker | None:
        """Return the ending marker for the glyph.

        Returns:
            Marker | None: The end marker element, or None if not applicable.
        """
        return None

    @classmethod
    def symbol(cls) -> Marker | None:
        """Return the symbol for the glyph.

        Returns:
            Marker | None: The symbol element, or None if not applicable.
        """
        return None

    def draw(self) -> BaseElement | None:
        """Draw the glyph and return an SVG element.

        Returns:
            BaseElement | None: The drawn SVG element, or None if not drawn.
        """
        return None

    @property
    def priority(self) -> int:
        """Return the priority of the glyph for sorting.

        Returns:
            int: The priority value of the glyph (default is 1).
        """
        return 1

    def __lt__(self, other: 'Glyph') -> bool:
        """Compare two glyphs based on their priority.

        Args:
            other (Glyph): The other glyph to compare with.

        Returns:
            bool: True if the current glyph has a lower priority than the other.
        """
        return self.priority < other.priority

    def __repr__(self) -> str:
        """Return a string representation of the Glyph.

        Returns:
            str: A string representing the Glyph instance.
        """
        return f"{self.__class__.__name__}('{self.class_name}')"

    @property
    def used_classes(self) -> set[Type['Glyph']]:
        """Return a set of all the classes that have contributed to this glyph.

        Returns:
            set[Type[Glyph]]: A set of classes from the class hierarchy that define this glyph.
        """
        return set(self.__class__.__mro__).difference({abc.ABC, object})
