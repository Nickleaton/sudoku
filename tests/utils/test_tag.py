"""TestTag."""

import unittest
from src.utils.tag import Tag, TagException


class TestTag(unittest.TestCase):
    """Test the Tag class."""

    def setUp(self) -> None:
        """Initialize a Tag instance for testing."""
        self.tag = Tag("Test")

    def test_name(self):
        """Verify that the tag's name is correctly initialized."""
        self.assertEqual("Test", self.tag.name)

    def test_repr(self):
        """Check that the repr() method returns the correct string representation."""
        self.assertEqual("Tag('Test')", repr(self.tag))

    def test_eq(self):
        """Test equality comparison between Tag instances."""
        self.assertEqual(Tag('one'), Tag('one'))
        self.assertNotEqual(Tag('one'), Tag('two'))
        with self.assertRaises(TagException):
            _ = self.tag == "xxx"

    def test_comparison(self):
        """Test comparison operators (<, <=) for Tag instances."""
        self.assertLess(Tag('alpha'), Tag('beta'))
        self.assertLessEqual(Tag('alpha'), Tag('beta'))
        with self.assertRaises(TagException):
            _ = self.tag < "xxx"
        with self.assertRaises(TagException):
            _ = self.tag <= "xxx"


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
