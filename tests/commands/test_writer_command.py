import unittest
from pathlib import Path

from src.commands.simple_command import SimpleCommand
from src.commands.svg_command import SVGCommand
from src.commands.writer_command import WriterCommand
from tests.commands.test_command import TestCommand


class TestWriterCommand(TestCommand):

    def setUp(self) -> None:
        self.child = SVGCommand(Path("problems\\easy\\problem001.yaml"))
        self.command = WriterCommand(self.child, Path("output\\solution\\problem001.txt"))
        self.command.file_name.unlink(missing_ok=True)

    def tearDown(self) -> None:
        self.command.file_name.unlink(missing_ok=True)

    def test_process(self):
        self.assertFalse(self.command.file_name.exists())
        self.command.process()
        self.assertTrue(self.command.file_name.exists())

    def clazz(self):
        return self.command.__class__.__name__

    @property
    def representation(self) -> str:
        return f"{self.clazz()}(SVGCommand('problems\\easy\\problem001.yaml'), 'output\\\\solution\\\\problem001.txt')"

    def test_repr(self):
        self.assertEqual(self.representation, repr(self.command))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
