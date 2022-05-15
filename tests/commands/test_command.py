import os
import unittest

from src.commands.command import Command


class TestCommand(unittest.TestCase):

    def setUp(self) -> None:
        self.command = Command(os.path.join('problems', 'problem001.yaml'), None)

    def test_command(self):
        self.command.process()
        self.assertIsNotNone(self.command.output)
        self.command.write()


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
