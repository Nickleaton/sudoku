"""XiPair."""

from src.items.sum_pair import SumPair


class XIPair(SumPair):
    """Represent an 'XI' pair, inheriting from `SumPair`."""

    @property
    def total(self) -> int:
        """Return the total number of the 'XI' pair.

        Returns:
            int: The total number for 'XI' pairs, which is 11.
        """
        return 11  # noqa: WPS432

    @property
    def tags(self) -> set[str]:
        """Return the set of tags associated with the 'XI' pair.

        Includes 'XI' along with the tags from the parent class.

        Returns:
            set[str]: A set of tags, including 'XI'.
        """
        return super().tags.union({'XI'})

    @property
    def label(self) -> str:
        """Return the label for the 'XI' pair.

        Returns:
            str: The label for this pair, which is 'XI'.
        """
        return 'XI'

    def css(self) -> dict[str, dict[str, str]]:
        """Return the CSS styles for the 'XI' pair.

        Defines and returns a start dictionary of CSS styles for the foreground
        and background elements.

        Returns:
            dict[str, dict[str, str]]: A dictionary containing CSS styles for
            both foreground and background elements.
        """
        return {
            '.XIPairForeground': {
                'font-size': '30px',
                'stroke': 'black',
                'stroke-width': '1',
                'fill': 'black',
            },
            '.XIPairBackground': {
                'font-size': '30px',
                'stroke': 'white',
                'stroke-width': '8',
                'fill': 'white',
                'font-weight': 'bolder',
            },
        }
