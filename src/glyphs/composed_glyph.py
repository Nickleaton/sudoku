from typing import List, Optional, Set, Type

from svgwrite.base import BaseElement
from svgwrite.container import Group

from src.glyphs.glyph import Glyph


class ComposedGlyph(Glyph):
    """Standard Composed Pattern for Glyphs
    """

    def __init__(self, class_name: str, items: Optional[List[Glyph]] = None):
        """Constructor

        :param class_name: The name of the class creating the glyph
        :param items: A list of glyphs to be grouped together
        """
        super().__init__(class_name)
        self.items = [] if items is None else items

    def __repr__(self) -> str:
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
        self.items.append(item)

    def draw(self) -> Optional[BaseElement]:
        group = Group()
        for glyph in sorted(self.items):
            group.add(glyph.draw())
        return group

    @property
    def used_classes(self) -> Set[Type[Glyph]]:
        result = super().used_classes
        result = result.union({ComposedGlyph})
        for item in self.items:
            result = result.union(item.used_classes)
        return result
