from src.glyphs.simple_text_glyph import SimpleTextGlyph
from src.utils.coord import Coord


class StarGlyph(SimpleTextGlyph):

    def __init__(self, class_name: str, position: Coord):
        super().__init__(class_name, 0, position, "✧")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.class_name}', {self.position!r})"
