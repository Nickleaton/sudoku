import unittest

from src.utils.tag import Tag, TagException


class TestTag(unittest.TestCase):

    def setUp(self) -> None:
        self.tag = Tag("Test")

    def test_name(self):
        self.assertEqual("Test", self.tag.name)

    def test_repr(self):
        self.assertEqual("Tag('Test')", repr(self.tag))

    def test_eq(self):
        self.assertEqual(Tag('one'), Tag('one'))
        self.assertNotEqual(Tag('one'), Tag('two'))
        with self.assertRaises(TagException):
            _ = self.tag == "xxx"

    def test_comparison(self):
        self.assertLess(Tag('alpha'), Tag('beta'))
        self.assertLessEqual(Tag('alpha'), Tag('beta'))
        with self.assertRaises(TagException):
            _ = self.tag < "xxx"
        with self.assertRaises(TagException):
            _ = self.tag <= "xxx"


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
