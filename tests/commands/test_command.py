import unittest

from src.commands.command import Command


class TestCommand(unittest.TestCase):

    def setUp(self) -> None:
        self.command = Command("output.txt")

    @property
    def representation(self) -> str:
        return r"Command('output.txt')"

    @property
    def output(self) -> str:
        return r"output.txt"

    def test_command(self):
        self.command.process()
        self.assertEqual(self.output, self.command.output_filename)
        self.command.write()

    def test_repr(self):
        self.assertEqual(self.representation, repr(self.command))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
