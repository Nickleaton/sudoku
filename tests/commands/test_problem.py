import unittest

from src.commands.problem import Problem


class TestProblem(unittest.TestCase):

    def setUp(self) -> None:
        self.problem = Problem()

    def test_set(self):
        self.assertEqual(0, len(self.problem))
        self.problem.name = "name"
        self.assertEqual("name", self.problem.name)
        self.assertEqual(1, len(self.problem))

    def test_clear(self):
        self.problem.name = "name"
        self.assertEqual(1, len(self.problem))
        self.problem.clear()
        self.assertEqual(None, self.problem.name)
        self.assertEqual(0, len(self.problem))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
