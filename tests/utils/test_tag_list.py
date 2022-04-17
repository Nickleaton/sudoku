import unittest

from src.utils.tag import Tag
from src.utils.tag_list import TagList, TagListException


class TestTagList(unittest.TestCase):

    def setUp(self) -> None:
        self.tags1 = TagList([Tag('beta'), Tag('alpha')])
        self.tags2 = TagList([Tag('beta'), Tag('gamma')])
        self.tags3 = TagList([Tag('beta')])
        self.tag = Tag('test')

    def test_iteration(self):
        i = 0
        for coord in self.tags1:
            i += 1
        self.assertEqual(i, len(self.tags1))

    def test_equality(self):
        self.assertEqual(self.tags1, self.tags1)
        self.assertNotEqual(self.tags1, self.tags2)
        self.assertNotEqual(self.tags1, self.tags3)
        with self.assertRaises(TagListException):
            _ = self.tags1 == "xxx"

    def test_contains(self):
        self.assertTrue(Tag('alpha') in self.tags1)
        self.assertFalse(Tag('omega') in self.tags1)

    def test_len(self):
        self.assertEqual(2, len(self.tags1))

    def test_repr(self):
        self.assertEqual("TagList([Tag('alpha'), Tag('beta')])", repr(self.tags1))

    def test_add(self):
        tags = TagList([Tag('beta'), Tag('alpha')])
        self.assertEqual(2, len(tags))
        tags.add(Tag("xxxx"))
        self.assertEqual(3, len(tags))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
