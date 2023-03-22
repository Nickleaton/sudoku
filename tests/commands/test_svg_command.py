import unittest
from pathlib import Path

from src.commands.svg_command import SVGCommand
from tests.commands.test_command import TestCommand


class TestSVGCommand(TestCommand):

    def setUp(self) -> None:
        self.command = SVGCommand('problems\\easy\\problem001.yaml')

    @property
    def output(self) -> Path:
        return Path("output\\svg\\problem001.svg")

    @property
    def representation(self) -> str:
        return "SVGCommand('problems\\easy\\problem001.yaml')"

    def test_repr(self):
        self.assertEqual(self.representation, repr(self.command))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
