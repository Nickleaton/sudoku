from src.glyphs.rectangle_glyph import RectangleGlyph
from src.utils.coord import Coord


class Consecutive1Glyph(RectangleGlyph):

    def __init__(self, class_name: str, first: Coord, second: Coord):
        vertical = first.column > second.column if first.row == second.row else first.row < second.row
        super().__init__(class_name, first, second, 0.25, 2.0, vertical)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.class_name}', {str(self.first)}, {str(self.second)})"
