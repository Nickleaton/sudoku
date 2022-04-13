from typing import List

from src.glyphs.glyph import Glyph, ConsecutiveGlyph
from src.items.less_than_equal_difference_pair import LessThanEqualDifferencePair
from src.utils.rule import Rule


class ConsecutivePair(LessThanEqualDifferencePair):

    @property
    def difference(self):
        return 1

    @property
    def rules(self) -> List[Rule]:
        return [Rule("ConsecutivePair", 1, "Cells separated by a white dot must be consecutive")]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Consecutive'})

    @property
    def glyphs(self) -> List[Glyph]:
        return [ConsecutiveGlyph(self.__class__.__name__, self.c1.coord.center, self.c2.coord.center)]
