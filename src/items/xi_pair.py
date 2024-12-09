"""XiPair."""

from src.items.sum_pair import SumPair


class XIPair(SumPair):
    """Represent an 'XI' pair, inheriting from `SumPair`."""

    @property
    def total(self) -> int:
        """Return the total number of the 'XI' pair.

        Return 11 as the total number for 'XI' pairs.
        """
        return 11

    @property
    def tags(self) -> set[str]:
        """Return the set of tags associated with the 'XI' pair.

        Include 'XI' along with the tags from the parent class.
        """
        return super().tags.union({'XI'})

    @property
    def label(self) -> str:
        """Return the label for the 'XI' pair.

        Return "XI" as the label for this pair.
        """
        return "XI"

    def css(self) -> dict:
        """Return the CSS styles for the 'XI' pair.

        Define and return start dictionary of CSS styles for the foreground
        and background elements.
        """
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
