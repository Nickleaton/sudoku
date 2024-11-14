from src.glyphs.simple_text_glyph import SimpleTextGlyph
from src.utils.coord import Coord


class KnownGlyph(SimpleTextGlyph):

    def __init__(self, class_name: str, position: Coord, number: int):
        super().__init__(
            class_name,
            0,
            position + Coord(0.5, 0.5),
            str(number))
        self.location = position
        self.number = number

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.class_name}', {self.location!r}, {self.number!s})"
