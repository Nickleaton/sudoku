from src.glyphs.text_glyph import TextGlyph
from src.utils.coord import Coord


class EdgeTextGlyph(TextGlyph):

    # pylint: disable=too-many-arguments
    def __init__(self, class_name: str, angle: float, first: Coord, second: Coord, text: str):
        super().__init__(class_name, angle, Coord.middle(first, second), text)
        self.first = first
        self.second = second

    @property
    def priority(self) -> int:
        return 5

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"("
            f"'{self.class_name}', "
            f"{self.angle.angle}, "
            f"{self.first!r}, "
            f"{self.second!r}, "
            f"'{self.text}'"
            f")"
        )
