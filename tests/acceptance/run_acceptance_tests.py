import unittest
from pathlib import Path

from tests.acceptance.acceptance_test import AcceptanceTest

# Directory containing test problem files
ACCEPTANCE_TEST_DIR = Path('problems/easy')

from tests.acceptance.acceptance_test import AcceptanceTest


def load_problem_tests():
    """Dynamically load problem files as individual test cases."""
    problem_files = [file.stem for file in ACCEPTANCE_TEST_DIR.glob("*.yaml")]

    for problem_name in problem_files:
        if problem_name != 'problem009':
            continue
        def test_method(self, problem_name=problem_name):
            test = AcceptanceTest(problem_name)
            test.test_all()

        # Assign a unique name to each test case method for unittest discovery
        setattr(AcceptanceTestSuite, f'test_{problem_name}', test_method)


class AcceptanceTestSuite(unittest.TestCase):
    """Test suite for dynamically loaded acceptance tests."""
    pass


load_problem_tests()  # Call to load problem tests

if __name__ == "__main__":
    unittest.main()