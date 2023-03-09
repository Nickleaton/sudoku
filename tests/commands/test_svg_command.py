import unittest

from src.commands.svg_command import SVGCommand
from tests.commands.test_command import TestCommand


class TestSVGcommand(TestCommand):

    def setUp(self) -> None:
        self.command = SVGCommand(r'problems/easy/problem001.yaml', r'output/svg/problem001.svg')

    @property
    def output(self) -> str:
        return r"output/svg/problem001.svg"

    def clazz(self) -> str:
        return SVGCommand

    @property
    def representation(self) -> str:
        return r"SVGCommand('problems/easy/problem001.yaml', 'output/svg/problem001.svg')"

    def test_repr(self):
        self.assertEqual(self.representation, repr(self.command))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
