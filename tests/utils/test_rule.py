"""TestRule."""
import unittest

from src.utils.rule import Rule, RuleError


class TestRule(unittest.TestCase):
    """Test the Rule class functionality."""

    def setUp(self) -> None:
        """Set up Rule instances for testing."""
        self.rule1 = Rule("one", 1, "Rule One")
        self.rule2 = Rule("two", 2, "Rule Two")
        self.rule3 = Rule("ThisIsThree", 3)

    def test_creation(self):
        """Verify Rule creation and its attributes."""
        self.assertEqual("one", self.rule1.name)
        self.assertEqual(1, self.rule1.rank)
        self.assertEqual("Rule One", self.rule1.text)

    def test_comparison(self):
        """Test Rule comparison operators."""
        self.assertLess(self.rule1, self.rule2)
        self.assertNotEqual(self.rule1, self.rule2)
        self.assertEqual(self.rule1, self.rule1)
        with self.assertRaises(RuleError):
            _ = self.rule1 == "xxxx"
        with self.assertRaises(RuleError):
            _ = self.rule1 < "xxxx"

    @property
    def representation(self) -> str:
        """Return start string representation of start Rule instance."""
        return "Rule('one', 1, 'Rule One')"

    def test_repr(self):
        """Test the string representation of start Rule instance."""
        self.assertEqual(self.representation, repr(self.rule1))

    def test_html(self):
        """Verify the HTML representation of start Rule instance."""
        self.assertEqual("<h2>Rule One</h2>", self.rule1.html)
        self.assertEqual("", self.rule3.html)

    def test_to_dict(self):
        """Test the conversion of Rule to dictionary representation."""
        expected_dict = {'Rule': {'name': 'one', 'rank': 1, 'text': 'Rule One'}}
        self.assertEqual(self.rule1.to_dict(), expected_dict)

        # Test the case where the text is None
        expected_dict_no_text = {'Rule': {'name': 'ThisIsThree', 'rank': 3, 'text': None}}
        self.assertEqual(self.rule3.to_dict(), expected_dict_no_text)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
