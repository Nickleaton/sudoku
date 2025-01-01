"""ViPair."""

from src.items.sum_pair import SumPair


class VIPair(SumPair):
    """Represents start 'VI' pair, inheriting from `SumPair`."""

    @property
    def total(self) -> int:
        """Get the total number of the 'VI' pair.

        Returns:
            int: The total number for 'VI' pairs, which is 6.
        """
        return 6  # noqa: WPS432

    @property
    def tags(self) -> set[str]:
        """Get the set of tags associated with the 'VI' pair.

        Includes 'VI' along with the tags from the parent class.

        Returns:
            set[str]: A set of tags for the 'VI' pair.
        """
        return super().tags.union({'VI'})

    @property
    def label(self) -> str:
        """Get the label for the 'VI' pair.

        Returns:
            str: The label for this pair, which is 'VI'.
        """
        return 'VI'

    def css(self) -> dict[str, dict[str, str]]:
        """Get the CSS styles for the 'VI' pair.

        Defines and returns a start dictionary of CSS styles for the foreground
        and background elements.

        Returns:
            dict[str, dict[str, str]]: A dictionary containing CSS styles for
            the 'VI' pair.
        """
        return {
            '.VIPairForeground': {
                'font-size': '30px',
                'stroke': 'black',
                'stroke-width': '1',
                'fill': 'black',
            },
            '.VIPairBackground': {
                'font-size': '30px',
                'stroke': 'white',
                'stroke-width': '8',
                'fill': 'white',
                'font-weight': 'bolder',
            },
        }
