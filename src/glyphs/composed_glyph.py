from typing import List, Optional, Set, Type

from svgwrite.base import BaseElement
from svgwrite.container import Group

from src.glyphs.glyph import Glyph


class ComposedGlyph(Glyph):
    """Group multiple glyphs together into a composed glyph.

    Use this class to group a set of `Glyph` objects into a single composed glyph.
    The `ComposedGlyph` acts as a container for its constituent `Glyph` objects,
    allowing you to add new items, draw them collectively on an SVG canvas, and
    retrieve all the used classes across the composition.

    Attributes:
        class_name (str): The CSS class name for the composed glyph.
        items (List[Glyph]): A list of `Glyph` objects to include in the composition.
    """

    def __init__(self, class_name: str, items: Optional[List[Glyph]] = None):
        """Initialize the ComposedGlyph with a given class name and optional items.

        Args:
            class_name (str): Set the CSS class name for the composed glyph.
            items (Optional[List[Glyph]], optional): Provide a list of `Glyph`
                objects to include in the composition. Default is an empty list.
        """
        super().__init__(class_name)
        self.items = [] if items is None else items

    def __repr__(self) -> str:
        """Return a string representation of the ComposedGlyph instance.

        Provide a human-readable string that shows the class name and the list of
        contained glyphs.

        Returns:
            str: Return a string representation of the ComposedGlyph instance.
        """
        return (
            f"{self.__class__.__name__}"
            f"("
            f"'{self.class_name}', "
            f"["
            f"{', '.join([str(item) for item in self.items])}"
            f"]"
            f")"
        )

    def add(self, item: Glyph):
        """Add a new `Glyph` to the composition.

        Append a `Glyph` object to the list of items in the composed glyph.

        Args:
            item (Glyph): Add a `Glyph` object to the composition.
        """
        self.items.append(item)

    def draw(self) -> Optional[BaseElement]:
        """Draw the composed glyph on an SVG canvas.

        Create an SVG `Group` element containing all the glyphs in the composition.
        Draw each glyph in sorted order.

        Returns:
            Optional[BaseElement]: Return an SVG `Group` element containing the
            glyphs, or `None` if no valid glyphs exist.
        """
        group = Group()
        for glyph in sorted(self.items):
            group.add(glyph.draw())  # Add each glyph to the group in sorted order
        return group

    @property
    def used_classes(self) -> Set[Type[Glyph]]:
        """Return all classes used by the composed glyph and its items.

        Collect and return a set of all the `Glyph` classes used by the composed
        glyph, including those used by its constituent items.

        Returns:
            Set[Type[Glyph]]: Return a set of all `Glyph` classes used in the
            composition.
        """
        result = super().used_classes  # Include the used classes from the parent class
        result = result.union({ComposedGlyph})  # Add the current class
        for item in self.items:
            result = result.union(item.used_classes)  # Add the used classes from each item
        return result
