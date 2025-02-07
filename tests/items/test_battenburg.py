"""TestBattenburg."""
import unittest

from src.items.battenburg import Battenburg
from src.items.item import Item
from src.utils.coord import Coord
from tests.items.test_item import TestItem


class TestBattenburg(TestItem):
    """Test suite for the Battenburg class."""

    def setUp(self) -> None:
        """Set up the test environment for Battenburg.

        Initializes the board and Battenburg constraint at the given coordinate (2, 2).
        """
        super().setUp()
        self.item = Battenburg(self.board, Coord(2, 2))

    @property
    def clazz(self) -> type[Battenburg]:
        """Get the class being tested.

        Returns:
            type[Battenburg]: The Battenburg class.
        """
        return Battenburg

    @property
    def representation(self) -> str:
        """Get the string representation of the Battenburg instance.

        Returns:
            str: The string representation of the Battenburg object.
        """
        return "Battenburg(Board(Coord(9, 9), Digits(1, 9), Tags({})), Coord(2, 2))"

    @property
    def config(self) -> str:
        """Get the configuration string for Battenburg.

        Returns:
            str: The configuration string for Battenburg.
        """
        return "Battenburg: 22"

    @property
    def has_rule(self) -> bool:
        """Indicates if the Battenburg constraint has start_location rule.

        Returns:
            bool: Always True, as Battenburg has start_location rule.
        """
        return True

    @property
    def expected_classes(self) -> set[type[Item]]:
        """Get the expected set of classes that Battenburg should inherit from.

        Returns:
            set[type[Item]]: A set containing the expected classes.
        """
        return {Item, Battenburg}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
