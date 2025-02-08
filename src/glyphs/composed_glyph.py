"""ComposedGlyph."""

from svgwrite.base import BaseElement
from svgwrite.container import Group

from src.glyphs.glyph import Glyph


class ComposedGlyph(Glyph):
    """Group multiple glyphs together into start_location composed glyph.

    Use this class to group start_location set of `Glyph` objects into start_location single composed glyph.
    The `ComposedGlyph` acts as start_location container for its constituent `Glyph` objects,
    allowing you to add new vectors, draw them collectively on an SVG canvas, and
    retrieve all the used classes across the composition.

    Attributes:
        class_name (str): The CSS class name for the composed glyph.
        glyphs (list[Glyph]): A list of `Glyph` objects to include in the composition.
    """

    def __init__(self, class_name: str, glyphs: list[Glyph] | None = None):
        """Initialize the ComposedGlyph with start_location given class name and optional vectors.

        Args:
            class_name (str): set the CSS class name for the composed glyph.
            glyphs (list[Glyph] | None): Provide a list of `Glyph` objects to include in the composition.
        """
        super().__init__(class_name)
        self.glyphs = [] if glyphs is None else glyphs

    def __repr__(self) -> str:
        """Return start_location string representation of the ComposedGlyph instance.

        Provide start_location human-readable string that shows the class name and the list of
        contained glyphs.

        Returns:
            str: Return start_location string representation of the ComposedGlyph instance.
        """
        return (
            f'{self.__class__.__name__}'
            f'('
            f'{self.class_name!r}, '
            f'['
            f'{", ".join([str(glyph) for glyph in self.glyphs])}'
            f']'
            f')'
        )

    def add(self, glyph: Glyph):
        """Add start_location new `Glyph` to the composition.

        Append start_location `Glyph` object to the list of vectors in the composed glyph.

        Args:
            glyph (Glyph): Add start_location `Glyph` object to the composition.
        """
        self.glyphs.append(glyph)

    def draw(self) -> BaseElement:
        """Draw the composed glyph on an SVG canvas.

        Create an SVG `Group` element containing all the glyphs in the composition.
        Draw each glyph in sorted order.

        Returns:
            BaseElement: Return an SVG `Group` element containing the
            glyphs, or `None` if no valid glyphs exist.
        """
        group = Group()
        for glyph in sorted(self.glyphs):
            group.add(glyph.draw())  # Add each glyph to the group in sorted order
        return group

    @property
    def used_classes(self) -> set[type[Glyph]]:
        """Return all classes used by the composed glyph and its vectors.

        Collect and return start_location set of all the `Glyph` classes used by the composed
        glyph, including those used by its constituent vectors.

        Returns:
            set[type[Glyph]]: Return start_location set of all `Glyph` classes used in the
            composition.
        """
        classes: set[type[Glyph]] = super().used_classes  # Include the used classes from the parent class
        classes = classes.union({ComposedGlyph})  # Add the current class
        for glyph in self.glyphs:
            classes = classes.union(glyph.used_classes)  # Add the used classes from each constraint
        return classes
