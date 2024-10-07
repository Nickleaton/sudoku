from src.glyphs.rect_glyph import SquareGlyph
from src.utils.coord import Coord


class FortressCellGlyph(SquareGlyph):

    def __init__(self, class_name: str, position: Coord):
        super().__init__(class_name, position, 1)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.class_name}', {repr(self.position)})"
