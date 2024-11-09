import re
import unittest

from src.tokens.token import Token, SequenceToken, ChoiceToken, RepeatToken, ZeroOrMoreToken, OneOrMoreToken, \
    OptionalToken


class TestToken(unittest.TestCase):
    """Test cases for the Token class and its operators."""

    def setUp(self):
        """Set up some example tokens to be used in the tests."""
        self.token = Token(r"A")
        self.token_a = Token(r"A")
        self.token_b = Token(r"B")
        self.name = "Token"
        self.good = ['A']
        self.bad = ['B']
        self.group_count = 0
        self.backus_naur = "<Token>"
        self.representation = "Token('A')"
        self.pattern = "A"

    def test_backus_naur_form(self):
        """Test the Backus-Naur form of the OneOrMoreToken."""
        self.assertEqual(self.backus_naur, self.token.backus_naur_form())

    def test_group_count(self):
        for text in self.good:
            self.assertEqual(len(self.token.groups(text)), self.group_count, "Incorrect group count")

    def test_add_operator_creates_sequence(self):
        """Test that the + operator creates a SequenceToken with the correct pattern."""
        result = self.token_a + self.token_b
        self.assertIsInstance(result, SequenceToken, "Expected a SequenceToken instance")
        self.assertEqual(result.pattern, "(A)(B)", "SequenceToken pattern is incorrect")

    def test_or_operator_creates_choice(self):
        """Test that the | operator creates a ChoiceToken with the correct pattern."""
        result = self.token_a | self.token_b
        self.assertIsInstance(result, ChoiceToken, "Expected a ChoiceToken instance")
        self.assertEqual(result.pattern, "(A)|(B)", "ChoiceToken pattern is incorrect")

    def test_mul_operator_creates_repeat_with_fixed_times(self):
        """Test that the * operator with an integer creates a RepeatToken with the correct pattern."""
        result = self.token_a * 3
        self.assertIsInstance(result, RepeatToken, "Expected a RepeatToken instance")
        self.assertEqual(result.pattern, "(A){3}", "RepeatToken pattern for fixed repetition is incorrect")

    def test_mul_operator_creates_repeat_with_range(self):
        """Test that the * operator with a tuple creates a RepeatToken with the correct pattern range."""
        result = self.token_a * (1, 5)
        self.assertIsInstance(result, RepeatToken, "Expected a RepeatToken instance")
        self.assertEqual(result.pattern, "(A){1,5}", "RepeatToken pattern for range repetition is incorrect")

    def test_name(self):
        self.assertEqual(self.name, self.token.name)

    def test_pattern_is_valid(self):
        """Test if the pattern is a valid regex pattern."""
        try:
            re.compile(self.token.pattern)
            is_valid = True
        except re.error:
            is_valid = False
        self.assertTrue(is_valid, "Pattern should be a valid regex.")

    def test_good(self):
        for text in self.good:
            self.assertTrue(self.token.match(text))

    def test_bad(self):
        for text in self.bad:
            self.assertFalse(self.token.match(text))

    def test_repr(self):
        """Test the string representation of the token."""
        self.assertEqual(repr(self.token), self.representation)

    def test_pattern(self):
        """Test that the pattern of the pattern is correct."""
        self.assertEqual(self.token.pattern, self.pattern)


class TestSequenceToken(TestToken):
    """Test cases for the SequenceToken class."""

    def setUp(self):
        """Set up example tokens specific for testing SequenceToken."""
        super().setUp()  # Call the parent class's setup
        self.token = SequenceToken([self.token_a, self.token_b])
        self.good = ['AB']
        self.bad = ['XX']
        self.name = "Sequence"
        self.group_count = 2
        self.backus_naur = "<Token> <Token>"
        self.pattern = '(A)(B)'
        self.representation = "SequenceToken(Token('A'), Token('B'))"


class TestRepeatToken(TestToken):
    """Test cases for the SequenceToken class."""

    def setUp(self):
        """Set up example tokens specific for testing SequenceToken."""
        super().setUp()  # Call the parent class's setup
        self.token = RepeatToken(Token("A"), 1, 2)
        self.good = ['AA', "A"]
        self.bad = ['XX', "AAA"]
        self.group_count = 1
        self.backus_naur = '<Token> {1,2}'
        self.name = 'Repeat'
        self.pattern = '(A){1,2}'
        self.representation = "RepeatToken(Token('A'), 1, 2)"


class TestChoiceToken(TestToken):
    """Test cases for the ChoiceToken class."""

    def setUp(self):
        """Set up example tokens specific for testing ChoiceToken."""
        super().setUp()  # Call the parent class's setup
        self.token = self.token_a | self.token_b  # Example choice token
        self.name = "Choice"
        self.good = ['A', 'B']
        self.bad = ['X']
        self.group_count = 2
        self.backus_naur = '(<Token> | <Token>)'
        self.pattern = '(A)|(B)'
        self.representation = "ChoiceToken(Token('A') | Token('B'))"


class TestOptionalToken(unittest.TestCase):
    """Test cases for the OptionalToken class."""

    def setUp(self):
        """Set up an example OptionalToken."""
        self.token_a = Token("A")
        self.token = OptionalToken(self.token_a)
        self.name = "Optional"
        self.good = ["", "A"]
        self.bad = ["AA", "B"]
        self.backus_naur = "xxx1"
        self.pattern = 'abc'
        self.representation = 'rep'


class TestOneOrMoreToken(unittest.TestCase):
    """Test cases for the OneOrMoreToken class."""

    def setUp(self):
        """Set up an example OneOrMoreToken."""
        self.token_a = Token("A")
        self.token = OneOrMoreToken(self.token_a)
        self.name = "OneOrMore"
        self.good = ["A", "AA", "AAA"]
        self.bad = ["", "B"]
        self.backus_naur = "xxx1"
        self.pattern = 'abc'
        self.representation = 'rep'


class TestZeroOrMoreToken(unittest.TestCase):
    """Test cases for the ZeroOrMoreToken class."""

    def setUp(self):
        """Set up an example ZeroOrMoreToken."""
        self.token_a = Token("A")
        self.token = ZeroOrMoreToken(self.token_a)
        self.name = "ZeroOrMore"
        self.good = ["", "A", "AA", "AAA"]
        self.bad = ["B"]
        self.backus_naur = "xxx1"
        self.pattern = 'abc'
        self.representation = 'rep'


if __name__ == "__main__":
    unittest.main()
