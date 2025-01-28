"""TestStatus."""
import unittest

from src.solvers.solver_status import SolverStatus


class TestSolverStatus(unittest.TestCase):
    """Test class for the SolverStatus enum."""

    def setUp(self):
        """Set up test cases."""
        self.valid_statuses = {
            'not_solved': SolverStatus.not_solved,
            'optimal': SolverStatus.optimal,
            'infeasible': SolverStatus.infeasible,
            'unbounded': SolverStatus.unbounded,
            'undefined': SolverStatus.undefined,
        }
        self.invalid_statuses = ['unknown', 'solved']

    def test_create_with_valid_statuses(self):
        """Test the create method with valid status strings."""
        for status_str, expected_status in self.valid_statuses.items():
            with self.subTest(status=status_str):
                self.assertEqual(SolverStatus.create(status_str), expected_status)

    def test_create_with_invalid_statuses(self):
        """Test the create method with invalid status strings."""
        for invalid_status in self.invalid_statuses:
            with self.subTest(status=invalid_status):
                with self.assertRaises(KeyError):
                    SolverStatus.create(invalid_status)

    def test_case_insensitivity(self):
        """Test that the create method handles case insensitivity."""
        self.assertEqual(SolverStatus.create('Optimal'), SolverStatus.optimal)
        self.assertEqual(SolverStatus.create('NOT_SOLVED'), SolverStatus.not_solved)
        self.assertEqual(SolverStatus.create('uNbOuNdEd'), SolverStatus.unbounded)


if __name__ == '__main__':
    unittest.main()
