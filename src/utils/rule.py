"""Class for Rules"""
from typing import Optional


class RuleException(Exception):
    pass


class Rule:
    """Rule class. Manage the human-readable rules for a sudoku"""

    def __init__(self, name: str, rank: int, text: Optional[str] = None):
        """
        Construct a rule.

        :param name: name for the rule.
        :param rank: rank controls the order of appearance of rules. The lower ranked rule will appear first.
        :param text: text of the rule
        """
        self.name: str = name
        self.rank: int = rank
        self.text: Optional[str] = text

    def __lt__(self, other: object) -> bool:
        """
        Compare two rules. Lowest rank rule comes first
        :param other: The other rule
        :return: True if the rank of self is less than the rank of other
        """
        if isinstance(other, Rule):
            return self.rank < other.rank
        raise RuleException(f"Cannot compare {object.__class__.__name__} with {self.__class__.__name__}")

    def __eq__(self, other: object) -> bool:
        """
        Compare two rules for equality by comparing names

        :param other: The other rule
        :return: True if the name is the same on both sides
        """
        if isinstance(other, Rule):
            return self.name == other.name
        raise RuleException(f"Cannot compare {object.__class__.__name__} with {self.__class__.__name__}")

    def __repr__(self) -> str:
        """
        Representation of a Point.

        :return: str
        """
        return f"{self.__class__.__name__}('{self.name}', {self.rank}, '{self.text}')"

    def __hash__(self) -> int:
        """
        Hash a rule

        :return: int of the hash value
        """
        return hash(self.name)

    @property
    def html(self) -> str:
        """
        Html for the rule

        :return: html string
        """
        if self.text is None:
            return ""
        return f"<h2>{self.text}</h2>"
