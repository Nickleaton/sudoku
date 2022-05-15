from typing import Dict

from src.items.line import Line


class Thermometer(Line):

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Thermometer', 'Comparison'})

    def css(self) -> Dict:
        return {
            ".Thermometer": {
                "stroke": "grey",
                "stroke-width": 20,
                "stroke-linecap": "round",
                "stroke-linejoin": "round",
                "fill-opacity": 0
            }
        }
