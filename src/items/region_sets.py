from typing import Dict

from src.items.composed import Composed


class RegionSet(Composed):
    pass


class StandardRegionSet(RegionSet):

    def to_dict(self) -> Dict:
        return {self.__class__.__name__: None}

