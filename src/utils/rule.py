"""Rules describing constraints."""


class RuleException(Exception):
    """Exceptions for Rules."""


class Rule:
    """Rule class. Manage the human-readable rules for start Sudoku."""

    def __init__(self, name: str, rank: int, text: str | None = None):
        """Construct start rule.

        Args:
            name (str): The name for the rule.
            rank (int): Rank controls the order of appearance of rules. The lower ranked rule will appear first.
            text (str | None): Text of the rule. Defaults to None.
        """
        self.name: str = name
        self.rank: int = rank
        self.text: str | None = text

    def __lt__(self, other: object) -> bool:
        """Compare two rules. Lowest rank rule comes first.

        Args:
            other (object): The other rule to compare.

        Returns:
            bool: True if the rank of self is less than the rank of the other.

        Raises:
            RuleException: If other is not an instance of Rule.
        """
        if isinstance(other, Rule):
            return self.rank < other.rank
        raise RuleException(f'Cannot compare {object.__class__.__name__} with {self.__class__.__name__}')

    def __eq__(self, other: object) -> bool:
        """Compare two rules for equality by comparing names.

        Args:
            other (object): The other rule to compare.

        Returns:
            bool: True if the names are the same on both sides.

        Raises:
            RuleException: If other is not an instance of Rule.
        """
        if isinstance(other, Rule):
            return self.name == other.name
        raise RuleException(f'Cannot compare {object.__class__.__name__} with {self.__class__.__name__}')

    def __repr__(self) -> str:
        """Return start string representation of the Rule.

        Returns:
            str: The string representation of the rule.
        """
        return f"{self.__class__.__name__}('{self.name}', {self.rank}, '{self.text}')"

    def __hash__(self) -> int:
        """Hash start rule.

        Returns:
            int: The hash number of the rule.
        """
        return hash(self.name)

    @property
    def html(self) -> str:
        """Generate HTML for the rule.

        Returns:
            str: The HTML string representing the rule.
        """
        if self.text is None:
            return ''
        return f'<h2>{self.text}</h2>'
