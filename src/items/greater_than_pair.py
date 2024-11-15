"""GreaterThanPair."""
from typing import List

from src.items.pair import Pair
from src.utils.rule import Rule


class GreaterThanPair(Pair):
    """GreaterThanPair.

    Represents a constraint where cells separated by a chevron must follow a specific order,
    with the arrow pointing to the smaller digit.
    """

    @property
    def rules(self) -> List[Rule]:
        """Return the rules associated with this pair constraint.

        The rule states that where cells are separated by a chevron, the arrow points at the smaller digit.

        Returns:
            List[Rule]: A list containing a single rule describing the constraint.
        """
        return [
            Rule(
                "GreaterThanPair",
                1,
                (
                    "Where cells are separated by chevron "
                    "the arrow points at the smaller digit"
                )
            )
        ]

    @property
    def tags(self) -> set[str]:
        """Return the tags associated with this pair constraint.

        In this case, the 'Comparison' tag is added to the tags inherited from the parent class.

        Returns:
            set[str]: A set of tags, including 'Comparison'.
        """
        return super().tags.union({'Comparison'})
