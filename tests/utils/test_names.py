"""TestNames."""
import unittest

from src.utils.names import Name


class TestNameConversions(unittest.TestCase):
    """Test the conversion methods of the Name class."""

    def test_camel_to_snake(self):
        """Convert camel_case to snake_case."""
        self.assertEqual(Name.camel_to_snake("BigTwoWordClass"), "big_two_word_class")
        self.assertEqual(Name.camel_to_snake("AnotherExample"), "another_example")
        self.assertEqual(Name.camel_to_snake("Single"), "single")
        self.assertEqual(Name.camel_to_snake(""), "")  # Test empty string

    def test_snake_to_camel(self):
        """Convert snake_case to camel_case."""
        self.assertEqual(Name.snake_to_camel("big_two_word_class"), "BigTwoWordClass")
        self.assertEqual(Name.snake_to_camel("another_example"), "AnotherExample")
        self.assertEqual(Name.snake_to_camel("single"), "Single")
        self.assertEqual(Name.snake_to_camel(""), "")  # Test empty string


if __name__ == "__main__":
    unittest.main()
