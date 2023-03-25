import unittest

from src.commands.command import Command


class TestCommand(unittest.TestCase):

    def setUp(self) -> None:
        self.command = Command()

    @property
    def representation(self) -> str:
        return r"Command()"

    # @property
    # def output(self) -> Path:
    #     return Path("output.txt")

    def test_command(self):
        self.command.execute()
        if self.__class__.__name__ == 'TestCommand':
            self.assertEqual(self.command.name, 'Command')
        else:
            self.assertEqual(self.command.name, self.__class__.__name__.replace("Test", "").replace("Command", ""))


    def test_repr(self):
        self.assertEqual(self.representation, repr(self.command))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
