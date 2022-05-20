from typing import Dict

from src.items.composed_item import ComposedItem


class RegionSet(ComposedItem):
    pass


class StandardRegionSet(RegionSet):

    def to_dict(self) -> Dict:
        return {self.__class__.__name__: None}
