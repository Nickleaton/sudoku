"""TestProblem."""
import unittest

from src.commands.problem import Problem


class TestProblem(unittest.TestCase):
    """Test suite for the Problem class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        self.problem = Problem()

    def test_set(self):
        """Test setting attributes on the Problem."""
        self.assertEqual(0, len(self.problem))
        self.problem.name = "name"
        self.assertEqual("name", self.problem.name)
        self.assertEqual(1, len(self.problem))

    def test_clear(self):
        """Test clearing attributes on the Problem."""
        self.problem.name = "name"
        self.assertEqual(1, len(self.problem))
        self.problem.clear()
        self.assertEqual(None, self.problem.name)
        self.assertEqual(0, len(self.problem))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
