import unittest
from pathlib import Path

from src.commands.img_command import IMGCommand
from src.commands.svg_command import SVGCommand
from tests.commands.test_command import TestCommand


class TestIMGCommand(TestCommand):

    def setUp(self) -> None:
        self.command = IMGCommand(SVGCommand(Path('problems\\easy\\problem001.yaml')), self.output)

    @property
    def output(self) -> Path:
        return Path("output\\jpg\\problem001.jpg")

    @property
    def representation(self) -> str:
        return r"IMGCommand(SVGCommand('problems\easy\problem001.yaml'), output\jpg\problem001.jpg)"

    def test_repr(self):
        self.assertEqual(self.representation, repr(self.command))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
