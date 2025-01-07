from src.validators.quadruple_validator import QuadrupleValidator
from tests.validators.test_validator import TestValidator


class TestQuadrupleValidator(TestValidator):
    """Test case for the QuadrupleValidator class."""

    def setUp(self):
        """Set up the specific test line for QuadrupleValidator."""
        super().setUp()
        self.valid_data = [
            {'quadruples': [1, 2]},
            {'quadruples': [1, 2, 3]},
            {'quadruples': [1, 2, '?']},
            {'quadruples': [1, 2, 2]},
            {'quadruples': [1, 2, 3, '?']},
            {'quadruples': [1, 2, 3, 4]},

        ]
        self.invalid_data = [
            {'questions': [1, 2, 3, 4, 5]},
            {'quadruples': [1, 2, 3, 10, '?', 5]},
            {'quadruples': []},
            {'quadruples': [0]},
            {'quadruples': [1, 2, 3, 4, 5]},
        ]
        self.validator = QuadrupleValidator()
        self.representation = 'QuadrupleValidator()'


if __name__ == '__main__':
    unittest.main()
