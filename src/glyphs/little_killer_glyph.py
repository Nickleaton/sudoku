"""LittleKillerGlyph."""
from svgwrite.base import BaseElement
from svgwrite.container import Group
from svgwrite.text import Text, TSpan

from src.glyphs.glyph import Glyph
from src.utils.angle import Angle
from src.utils.config import Config
from src.utils.point import Point

config: Config = Config()


class LittleKillerGlyph(Glyph):
    """Represents a Little Killer Sudoku glyph with an arrow and number."""

    arrow: str = '\uA71B'  # ꜛ

    def __init__(self, class_name: str, position: Point, angle: Angle, input_value: int) -> None:
        """Initialize the Little Killer glyph with class name, position, angle, and input_value.

        Args:
            class_name (str): The CSS class name for styling the glyph.
            position (Point): The coordinate position of the glyph.
            angle (Angle): The angle of the glyph's arrow.
            input_value (int): The numerical input_value associated with the glyph.
        """
        super().__init__(class_name)
        self.position: Point = position
        self.angle: Angle = angle
        self.input_value: int = input_value

    def draw(self) -> BaseElement | None:
        """Create an SVG representation of the Little Killer glyph.

        Returns:
            BaseElement | None: A group containing the arrow and number elements,
            or None if the glyph cannot be drawn.
        """
        group: Group = Group()
        # Positioning the text slightly offset
        offset: Point = Point(
            config.graphics.little_killer_offset_percentage,
            config.graphics.little_killer_offset_percentage,
        )
        adjusted_position: Point = (self.position + offset).center
        # Create number text element
        number_text: Text = Text(
            '',
            transform=adjusted_position.transform,
            class_=self.class_name,
        )
        number_span: TSpan = TSpan(str(self.input_value), alignment_baseline='central', text_anchor='middle')
        number_text.add(number_span)
        group.add(number_text)

        # Create arrow text element
        arrow_text: Text = Text(
            '',
            transform=f'{adjusted_position.transform} {self.angle.transform}',
            class_=self.class_name,
        )
        arrow_span: TSpan = TSpan(self.arrow, alignment_baseline='central', text_anchor='middle')
        arrow_text.add(arrow_span)
        group.add(arrow_text)

        return group

    def __repr__(self) -> str:
        """Return string representation of the Little Killer glyph.

        Returns:
            str: The string representation of the glyph, including class name,
            position, angle, and number.
        """
        return (
            f'{self.__class__.__name__}('
            f'{self.class_name!r}, '
            f'{self.position!r}, '
            f'{self.angle!r}, '
            f'{self.input_value!r}'
            f')'
        )
