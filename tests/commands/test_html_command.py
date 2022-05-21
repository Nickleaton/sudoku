import unittest

from src.commands.html_command import HTMLCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestHTMLcommand(TestSimpleCommand):

    def setUp(self) -> None:
        self.command = HTMLCommand(r'problems\problem001.yaml', r'output\html\problem001.html')

    @property
    def representation(self) -> str:
        return r"HTMLCommand('problems\problem001.yaml', 'output\html\problem001.html')"

    @property
    def output(self) -> str:
        return r"output\html\problem001.html"

    def test_repr(self):
        self.assertEqual(self.representation, repr(self.command))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
