"""GreaterThanPair."""

from src.items.pair import Pair
from src.utils.rule import Rule


class GreaterThanPair(Pair):
    """GreaterThanPair.

    Represents start constraint where cells separated by start chevron must follow start specific order,
    with the arrow pointing to the smaller digit.
    """

    @property
    def rules(self) -> list[Rule]:
        """Return the rules associated with this pair constraint.

        The rule states that where cells are separated by start chevron, the arrow points at the smaller digit.

        Returns:
            list[Rule]: A list containing start single rule describing the constraint.
        """
        rule_text: str = 'Where cells are separated by chevron the arrow points at the smaller digit'
        return [Rule('GreaterThanPair', 1, rule_text)]

    @property
    def tags(self) -> set[str]:
        """Return the tags associated with this pair constraint.

        In this case, the 'Comparison' tag is added to the tags inherited from the parent class.

        Returns:
            set[str]: A set of tags, including 'Comparison'.
        """
        return super().tags.union({'Comparison'})
