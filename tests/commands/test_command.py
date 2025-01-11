import unittest
from pathlib import Path

from src.commands.command import Command
from src.commands.problem import Problem
from src.utils.load_modules import load_modules


class TestCommand(unittest.TestCase):
    """Test suite for the Command class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        load_modules('items')
        self.command = Command()
        self.problem = Problem(
            problem_file_name=Path('problems/easy/problem001.yaml'),
            output_directory=Path('output/tests/'),
        )
        self.empty_problem = Problem(Path('problems/easy/problem001.yaml'), Path('output/tests/'))
        self.config_file: Path = Path(r'problems\easy\problem001.yaml')
        self.missing_file: Path = Path(r'output\tests\nonexistent.txt')
        self.readable_file: Path = Path(r'output\tests\output.txt')
        self.writable_file: Path = Path(r'output\tests\output.txt')
        self.readable_file.parent.mkdir(parents=True, exist_ok=True)
        with self.readable_file.open('w') as f:
            f.write('Hello World')
        if self.writable_file.exists():
            self.writable_file.unlink()
        self.representation = 'Command()'

    def tearDown(self):
        """Clean up the test environment."""
        if self.readable_file.exists():
            self.readable_file.unlink()
        if self.writable_file.exists():
            self.writable_file.unlink()

    def test_command_name(self):
        """Test the name property of the Command class."""
        if self.command is None:
            return
        expected_name: str = 'Command' \
            if self.__class__.__name__ == 'TestCommand' \
            else self.__class__.__name__.replace('Test', "").replace('Command', "")
        self.assertEqual(self.command.name, expected_name)

    def test_command_execute(self):
        """Test the execute method of the Command class."""
        if self.command is None:
            return
        self.command.execute(self.problem)

    def test_repr(self):
        """Test the __repr__ method of the Command class."""
        if self.command is None:
            return
        self.assertEqual(self.representation, repr(self.command))

    def test_target(self):
        """Test the target property of the Command class."""
        if self.command is None:
            return
        if isinstance(self.command, Command):
            self.assertIsNone(self.command.target)
        else:
            self.assertIsNotNone(self.command.target)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
