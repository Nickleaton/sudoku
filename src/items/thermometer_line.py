from typing import Dict
from src.items.line import Line


class ThermometerLine(Line):
    """Represents a thermometer line in a puzzle, typically used to indicate a
    comparison between digits.
    """

    @property
    def tags(self) -> set[str]:
        """Tags associated with the Thermometer line.

        Returns:
            set[str]: A set of tags specific to the Thermometer line, combined with inherited tags.
        """
        return super().tags.union({'ThermometerLine', 'Comparison'})

    def css(self) -> Dict:
        """CSS styling properties for rendering the Thermometer line.

        Returns:
            Dict: A dictionary defining CSS properties for the Thermometer line.
        """
        return {
            ".ThermometerLine": {
                "stroke": "grey",
                "stroke-width": 25,
                "stroke-linecap": "round",
                "stroke-linejoin": "round",
                "fill-opacity": 0
            }
        }
