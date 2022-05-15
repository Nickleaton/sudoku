from typing import Dict

from src.items.sum_pair import SumPair


class VIPair(SumPair):

    @property
    def total(self) -> int:
        return 6

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'VI'})

    @property
    def label(self) -> str:
        return "VI"

    def css(self) -> Dict:
        return {
            ".VIPairForeground": {
                "font-size": "30px",
                "stroke": "black",
                "stroke-width": 1,
                "fill": "black"
            },
            ".VIPairBackground": {
                "font-size": "30px",
                "stroke": "white",
                "stroke-width": 8,
                "fill": "white",
                "font-weight": "bolder"
            }
        }
