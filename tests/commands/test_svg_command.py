"""TestSvgCommand."""
import unittest
from pathlib import Path

from src.commands.create_board_command import CreateBoardCommand
from src.commands.create_constraints_command import CreateConstraintsCommand
from src.commands.file_reader_command import FileReaderCommand
from src.commands.load_config_command import LoadConfigCommand
from src.commands.svg_command import SVGCommand
from src.items.item import Item
from tests.commands.test_simple_command import TestSimpleCommand


class TestSVGCommand(TestSimpleCommand):
    """Test suite for the SVGCommand class."""

    def setUp(self) -> None:
        """Sets up the test environment for SVGCommand."""
        super().setUp()
        self.prerequisites = (
                FileReaderCommand(
                    file_name="config_file_name",
                    target="config_text",
                    file_path=Path("problems\\easy\\problem001.yaml"),
                )
                | LoadConfigCommand()
                | CreateBoardCommand()
                | CreateConstraintsCommand()
        )
        self.prerequisites.execute(self.problem)
        self.command = SVGCommand()
        self.representation = "SVGCommand('board', 'constraints', 'svg')"

    def test_in_select(self):
        """Tests the `select` method for the `in_select` item.

        If the `in_select` property is not `None`, verifies that the
        `select` method of the command returns `True` for the item.
        """
        if (select := self.in_select) is not None:
            self.assertTrue(self.command.select(select))

    def test_out_select(self):
        """Tests the `select` method for the `out_select` item.

        If the `out_select` property is not `None`, verifies that the
        `select` method of the command returns `False` for the item.
        """
        if (select := self.out_select) is not None:
            self.assertFalse(self.command.select(select))

    @property
    def in_select(self) -> Item | None:
        """Gets an item that should be included in the output of the command.

        Returns:
            Item | None: An item that should be included in the output, or `None`.
        """
        return None

    @property
    def out_select(self) -> Item | None:
        """Gets an item that should not be included in the output of the command.

        Returns:
            Item | None: An item that should not be included in the output, or `None`.
        """
        return None


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
