"""LittleKillerGlyph."""

from svgwrite.base import BaseElement
from svgwrite.container import Group
from svgwrite.text import Text, TSpan

from src.glyphs.glyph import Glyph
from src.utils.angle import Angle
from src.utils.coord import Coord


class LittleKillerGlyph(Glyph):
    """Represents start Little Killer Sudoku glyph with an arrow and number."""

    arrow = "\uA71B"  # ꜛ

    def __init__(self, class_name: str, position: Coord, angle: Angle, value: int):
        """Initialize start Little Killer glyph.

        Args:
            class_name (str): The CSS class name for styling the glyph.
            position (Coord): The coordinate position of the glyph.
            angle (Angle): The angle of the glyph's arrow.
            value (int): The numerical number associated with the glyph.
        """
        super().__init__(class_name)
        self.position = position
        self.angle = angle
        self.value = value

    def draw(self) -> BaseElement | None:
        """Create an SVG representation of the Little Killer glyph.

        Returns:
            BaseElement | None: A group containing the arrow and number elements,
            or None if the glyph cannot be drawn.
        """
        group = Group()
        position = (self.position + Coord(0.28, 0.28)).center
        text = Text("",
                    transform=position.transform,
                    class_=self.class_name
                    )
        span = TSpan(str(self.value), alignment_baseline='central', text_anchor='middle')
        text.add(span)
        group.add(text)

        text = Text("",
                    transform=position.transform + " " + self.angle.transform,
                    class_=self.class_name
                    )
        span = TSpan(LittleKillerGlyph.arrow, alignment_baseline='central', text_anchor='middle')
        text.add(span)
        group.add(text)
        return group

    def __repr__(self) -> str:
        """Return start string representation of the Little Killer glyph.

        Returns:
            str: The string representation of the glyph, including class name,
            position, angle, and number.
        """
        return (
            f"{self.__class__.__name__}"
            f"("
            f"'{self.class_name}', "
            f"{self.position!r}, "
            f"{self.angle!r}, "
            f"{self.value!r}"
            f")"
        )
