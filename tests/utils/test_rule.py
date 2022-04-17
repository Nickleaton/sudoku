import unittest

from src.utils.rule import Rule, RuleException


class TestRule(unittest.TestCase):

    def setUp(self) -> None:
        self.rule1 = Rule("one", 1, "Rule One")
        self.rule2 = Rule("two", 2, "Rule Two")
        self.rule3 = Rule("ThisIsThree", 3)

    def test_creation(self):
        self.assertEqual("one", self.rule1.name)
        self.assertEqual(1, self.rule1.rank)
        self.assertEqual("Rule One", self.rule1.text)

    def test_comparison(self):
        self.assertLess(self.rule1, self.rule2)
        self.assertNotEqual(self.rule1, self.rule2)
        self.assertEqual(self.rule1, self.rule1)
        with self.assertRaises(RuleException):
            _ = self.rule1 == "xxxx"
        with self.assertRaises(RuleException):
            _ = self.rule1 < "xxxx"

    @property
    def representation(self) -> str:
        return "Rule('one', 1, 'Rule One')"

    def test_repr(self):
        self.assertEqual(self.representation, repr(self.rule1))

    def test_html(self):
        self.assertEqual("<h2>Rule One</h2>", self.rule1.html)
        self.assertEqual("", self.rule3.html)

    def test_human_name(self):
        self.assertEqual("This Is Three", self.rule3.human_name)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
