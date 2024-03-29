import unittest
from pathlib import Path

from src.commands.html_command import HTMLCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestHTMLCommand(TestSimpleCommand):

    def setUp(self) -> None:
        self.command = HTMLCommand(Path('problems\\easy\\problem001.yaml'))

    @property
    def representation(self) -> str:
        return "HTMLCommand('problems\\easy\\problem001.yaml')"

    def test_repr(self):
        self.assertEqual(self.representation, repr(self.command))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
