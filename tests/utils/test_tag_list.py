"""TestTagList."""

import unittest

from src.utils.tag import Tag
from src.utils.tag_list import TagList, TagListException


class TestTagList(unittest.TestCase):
    """Test the TagList class."""

    def setUp(self) -> None:
        """Initialize TagList instances for testing."""
        self.tags1 = TagList([Tag('beta'), Tag('alpha')])
        self.tags2 = TagList([Tag('beta'), Tag('gamma')])
        self.tags3 = TagList([Tag('beta')])
        self.tag = Tag('test')

    def test_iteration(self):
        """Test iteration over the TagList."""
        i = 0
        for _ in self.tags1:
            i += 1
        self.assertEqual(i, len(self.tags1))

    def test_tag_list_len(self):
        """Verify the length of the TagList."""
        self.assertEqual(2, len(self.tags1))

    def test_tag_list_iterator(self):
        """Test that TagList iteration returns vectors in correct order."""
        iterated_items = list(self.tags1)
        for idx, vector in enumerate(iterated_items):
            self.assertEqual(vector, self.tags1[idx])

    def test_equality(self):
        """Test equality comparison for TagList instances."""
        self.assertEqual(self.tags1, self.tags1)
        self.assertNotEqual(self.tags1, self.tags2)
        self.assertNotEqual(self.tags1, self.tags3)
        with self.assertRaises(TagListException):
            _ = self.tags1 == "xxx"

    def test_contains(self):
        """Test membership check for TagList."""
        self.assertTrue(Tag('alpha') in self.tags1)
        self.assertFalse(Tag('omega') in self.tags1)

    def test_len(self):
        """Test length of the TagList."""
        self.assertEqual(2, len(self.tags1))

    def test_repr(self):
        """Verify the string representation of the TagList."""
        self.assertEqual("TagList([Tag('alpha'), Tag('beta')])", repr(self.tags1))

    def test_add(self):
        """Test adding start new tag to the TagList."""
        tags = TagList([Tag('beta'), Tag('alpha')])
        self.assertEqual(2, len(tags))
        tags.add(Tag("xxxx"))
        self.assertEqual(3, len(tags))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
