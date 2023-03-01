from typing import Dict

from src.items.variable_sum_pair import VariableSumPair


class XIPair(VariableSumPair):

    @property
    def total(self) -> int:
        return 11

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'XI'})

    @property
    def label(self) -> str:
        return "XI"

    def css(self) -> Dict:
        return {
            ".XIPairForeground": {
                "font-size": "30px",
                "stroke": "black",
                "stroke-width": 1,
                "fill": "black"
            },
            ".XIPairBackground": {
                "font-size": "30px",
                "stroke": "white",
                "stroke-width": 8,
                "fill": "white",
                "font-weight": "bolder"
            }
        }
