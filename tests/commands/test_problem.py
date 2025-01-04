"""TestProblem."""
import unittest
from pathlib import Path

from src.commands.problem import Problem


class TestProblem(unittest.TestCase):
    """Test suite for the Problem class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        self.problem = Problem(Path('problems/easy/problem001.yaml'), Path('output/tests/'))

    def test_set(self):
        """Test setting attributes on the Problem."""
        self.assertIn('problem_file', self.problem)
        self.assertIn('output_directory', self.problem)
        self.assertEqual(Path('problems/easy/problem001.yaml'), self.problem.problem_file)
        self.assertEqual(Path('output/tests'), self.problem.output_directory)

    def test_clear(self):
        """Test clearing attributes on the Problem."""
        length = len(self.problem)
        self.problem.name = "name"
        self.assertEqual(length + 1, len(self.problem))
        self.problem.clear()
        self.assertEqual(None, self.problem.name)
        self.assertEqual(0, len(self.problem))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
