"""ViPair."""
from typing import dict

from src.items.sum_pair import SumPair


class VIPair(SumPair):
    """Represent a 'VI' pair, inheriting from `SumPair`."""

    @property
    def total(self) -> int:
        """Return the total value of the 'VI' pair.

        Return 6 as the total value for 'VI' pairs.
        """
        return 6

    @property
    def tags(self) -> set[str]:
        """Return the set of tags associated with the 'VI' pair.

        Include 'VI' along with the tags from the parent class.
        """
        return super().tags.union({'VI'})

    @property
    def label(self) -> str:
        """Return the label for the 'VI' pair.

        Return "VI" as the label for this pair.
        """
        return "VI"

    def css(self) -> dict:
        """Return the CSS styles for the 'VI' pair.

        Define and return a dictionary of CSS styles for the foreground
        and background elements.
        """
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
