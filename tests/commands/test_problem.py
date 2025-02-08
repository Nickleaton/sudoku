"""TestProblem."""
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from src.commands.problem import Problem


class TestProblem(unittest.TestCase):
    """Test cases for the Problem class."""

    def setUp(self) -> None:
        """Set up temporary files and directories for testing."""
        self.valid_problem_file = Path('valid_problem_file.txt')
        self.invalid_problem_file = Path('invalid_problem_file.txt')

        # Create a valid problem file in a temporary directory
        self.temp_dir = TemporaryDirectory()  # pylint: disable=consider-using-with
        self.valid_problem_file = Path(self.temp_dir.name) / 'valid_problem_file.txt'
        self.valid_problem_file.touch()  # Create the file

        self.output_directory = Path(self.temp_dir.name) / 'output'
        self.output_directory.mkdir()  # Create output directory

    def tearDown(self) -> None:
        """Clean up temporary files and directories."""
        self.temp_dir.cleanup()

    def test_initialize_with_valid_inputs(self):
        """Test initialization with valid file and output directory."""
        problem = Problem(self.valid_problem_file, self.output_directory)
        self.assertEqual(problem.problem_file_name, self.valid_problem_file)
        self.assertEqual(problem.output_directory, self.output_directory)
        self.assertIsNone(problem.constraints)
        self.assertIsNone(problem.raw_config)
        self.assertIsNone(problem.config)

    def test_initialize_with_missing_problem_file(self):
        """Test initialization with a missing problem file."""
        with self.assertRaises(FileNotFoundError):
            Problem(self.invalid_problem_file, self.output_directory)

    def test_initialize_with_invalid_output_directory(self):
        """Test initialization with an invalid output directory."""
        invalid_output_file = self.valid_problem_file  # A file instead of a directory
        with self.assertRaises(NotADirectoryError):
            Problem(self.valid_problem_file, invalid_output_file)

    def test_str_representation(self):
        """Test the string representation of the Problem class."""
        problem = Problem(self.valid_problem_file, self.output_directory)
        expected_str = (
            f'Problem file: {self.valid_problem_file}, '
            f'Output directory: {self.output_directory}'
        )
        self.assertEqual(str(problem), expected_str)

    def test_repr_representation(self):
        """Test the repr representation of the Problem class."""
        problem = Problem(self.valid_problem_file, self.output_directory)
        expected_repr = (
            f'Problem('
            f'problem_file_name={self.valid_problem_file!r}, '
            f'output_directory={self.output_directory!r}, '
            f'solver=None)'
        )
        self.assertEqual(repr(problem), expected_repr)


if __name__ == "__main__":
    unittest.main()
