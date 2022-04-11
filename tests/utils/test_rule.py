import unittest

from src.utils.rule import Rule


class TestRule(unittest.TestCase):

    def setUp(self) -> None:
        self.r1 = Rule("one", 1, "Rule One")
        self.r2 = Rule("two", 2, "Rule Two")
        self.r3 = Rule("ThisIsThree", 3, None)

    def test_creation(self):
        self.assertEqual("one", self.r1.name)
        self.assertEqual(1, self.r1.rank)
        self.assertEqual("Rule One", self.r1.text)

    def test_comparison(self):
        self.assertLess(self.r1, self.r2)
        self.assertNotEqual(self.r1, self.r2)
        self.assertEqual(self.r1, self.r1)

    @property
    def representation(self) -> str:
        return "Rule('one', 1, 'Rule One')"

    def test_repr(self):
        self.assertEqual(self.representation, repr(self.r1))

    def test_html(self):
        self.assertEqual("<h2>Rule One</h2>", self.r1.html)
        self.assertEqual("", self.r3.html)

    def test_human_name(self):
        self.assertEqual("This Is Three", self.r3.human_name)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
