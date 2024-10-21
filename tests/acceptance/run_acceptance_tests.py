import os
import unittest
from pathlib import Path

import pytest

from tests.acceptance.acceptance_test import AcceptanceTest

# Directory containing test problem files
ACCEPTANCE_TEST_DIR = Path('problems/easy')


@pytest.mark.parametrize("problem_name", [
    file_name.replace('.yaml', '')  # Assuming problem names map to file names
    for file_name in os.listdir(ACCEPTANCE_TEST_DIR) if file_name.endswith('.yaml')
])
def test_all(problem_name: str):
    test = AcceptanceTest(problem_name)
    test.test_all()

if __name__ == "__main__":
    unittest.main()
