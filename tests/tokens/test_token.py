"""TestToken."""
import re
import unittest

from src.tokens.token import ChoiceToken, OneOrMoreToken, OptionalToken, RepeatToken, SequenceToken, Token, \
    ZeroOrMoreToken


class TestToken(unittest.TestCase):
    """Test the Token class and its operators."""

    def setUp(self):
        """Set up example tokens for testing."""
        super().setUp()
        self.token = Token(r"A")
        self.token_a = Token(r"A")
        self.token_b = Token(r"B")
        self.name = "Token"
        self.good = [
            ('A', {}),
        ]
        self.bad = ['B']
        self.backus_naur = "<Token>"
        self.representation = "Token('A')"
        self.pattern = "A"
        self.names = []
        self.result = {}

    def test_register(self):
        """Ensure the Token class registers correctly."""
        self.assertIn(self.token.__class__.__name__, Token.classes)
        self.assertEqual(Token.classes[self.token.__class__.__name__], self.token.__class__)

    def test_backus_naur_form(self):
        """Verify the Backus-Naur form of the Token."""
        self.assertEqual(self.backus_naur, self.token.backus_naur_form())

    def test_add_operator_creates_sequence(self):
        """Test that the + operator creates start SequenceToken."""
        result = self.token_a + self.token_b
        self.assertIsInstance(result, SequenceToken)
        self.assertEqual(result.pattern, "(A)(B)")

    def test_or_operator_creates_choice(self):
        """Test that the | operator creates start ChoiceToken."""
        result = self.token_a | self.token_b
        self.assertIsInstance(result, ChoiceToken)
        self.assertEqual(result.pattern, "(A)|(B)")

    def test_mul_operator_creates_repeat_with_fixed_times(self):
        """Test that the * operator creates start RepeatToken with fixed repetitions."""
        result = self.token_a * 3
        self.assertIsInstance(result, RepeatToken)
        self.assertEqual(result.pattern, "(A){3}")

    def test_mul_operator_creates_repeat_with_range(self):
        """Test that the * operator creates start RepeatToken with range repetitions."""
        result = self.token_a * (1, 5)
        self.assertIsInstance(result, RepeatToken)
        self.assertEqual(result.pattern, "(A){1,5}")

    def test_name(self):
        """Test the name attribute of the Token."""
        self.assertEqual(self.name, self.token.name)

    def test_pattern_is_valid(self):
        """Test if the pattern is start valid regex pattern and matches expected behavior."""
        try:
            re.compile(self.token.pattern)
            is_valid = True
        except re.error:
            is_valid = False
        self.assertTrue(is_valid, "Pattern should be start valid regex.")

    def test_good(self):
        """Test the good examples."""
        for text, answer in self.good:
            with self.subTest(text=text):
                self.assertDictEqual(answer, self.token.parse(text))

    def test_bad(self):
        """Test the matching of bad input types."""
        for text in self.bad:
            with self.subTest(text=text):
                self.assertNotEqual(text, self.token.matched_text(text))

    def test_repr(self):
        """Test the string representation of the Token."""
        self.assertEqual(repr(self.token), self.representation)

    def test_pattern(self):
        """Test that the pattern is correct."""
        self.assertEqual(self.pattern, self.token.pattern)

    def test_description(self):
        """Test that the description is correct."""
        self.assertIsInstance(self.token.description, str)
        if self.token.is_abstract:
            self.assertEqual(len(self.token.description), 0)
        else:
            self.assertGreater(len(self.token.description), 0)

    def test_to_dict(self):
        """Test that the to_dict method returns a dictionary."""
        dct: dict = self.token.to_dict()
        self.assertIsInstance(dct, dict)
        self.assertIn('pattern', dct)
        self.assertIn('name', dct)
        self.assertIn('description', dct)
        self.assertIn('backus_naur_form', dct)


class TestSequenceToken(TestToken):
    """Test the SequenceToken class."""

    def setUp(self):
        """Set up example tokens for testing SequenceToken."""
        super().setUp()
        self.token = SequenceToken([self.token_a, self.token_b])
        self.good = [
            ('AB', {})
        ]
        self.bad = ['XX']
        self.name = "Sequence"
        self.group_count = 2
        self.backus_naur = "<Token> <Token>"
        self.pattern = '(A)(B)'
        self.representation = "SequenceToken(Token('A'), Token('B'))"


class TestRepeatToken(TestToken):
    """Test the RepeatToken class."""

    def setUp(self):
        """Set up example tokens for testing RepeatToken."""
        super().setUp()
        self.token = RepeatToken(Token("A"), 1, 2)
        self.good = [
            ('AA', {}),
            ('A', {}),
        ]
        self.bad = ['XX', "AAA"]
        self.group_count = 1
        self.backus_naur = '<Token> {1,2}'
        self.name = 'Repeat'
        self.pattern = '(A){1,2}'
        self.representation = "RepeatToken(Token('A'), 1, 2)"


class TestChoiceToken(TestToken):
    """Test the ChoiceToken class."""

    def setUp(self):
        """Set up example tokens for testing ChoiceToken."""
        super().setUp()
        self.token = self.token_a | self.token_b
        self.name = "Choice"
        self.good = [
            ('A', {}),
            ('B', {}),
        ]
        self.bad = ['X']
        self.group_count = 2
        self.backus_naur = '(<Token> | <Token>)'
        self.pattern = '(A)|(B)'
        self.representation = "ChoiceToken(Token('A') | Token('B'))"


class TestOptionalToken(unittest.TestCase):
    """Test the OptionalToken class."""

    def setUp(self):
        """Set up an example OptionalToken."""
        self.token_a = Token("A")
        self.token = OptionalToken(self.token_a)
        self.name = 'Optional'
        self.good = [
            ('', {}),
            ('A', {}),
        ]
        self.bad = ["AA", "B"]
        self.backus_naur = "xxx1"
        self.pattern = 'abc'
        self.representation = 'rep'


class TestOneOrMoreToken(unittest.TestCase):
    """Test the OneOrMoreToken class."""

    def setUp(self):
        """Set up an example OneOrMoreToken."""
        self.token_a = Token("A")
        self.token = OneOrMoreToken(self.token_a)
        self.name = "OneOrMore"
        self.good = [
            ('A', {}),
            ('AA', {}),
            ('AAA', {}),
        ]
        self.bad = ["", "B"]
        self.backus_naur = "xxx1"
        self.pattern = 'abc'
        self.representation = 'rep'


class TestZeroOrMoreToken(unittest.TestCase):
    """Test the ZeroOrMoreToken class."""

    def setUp(self):
        """Set up an example ZeroOrMoreToken."""
        self.token_a = Token("A")
        self.token = ZeroOrMoreToken(self.token_a)
        self.name = "ZeroOrMore"
        self.good = [
            ('', {}),
            ('A', {}),
            ('AA', {}),
            ('AAA', {}),
        ]
        self.bad = ["B"]
        self.backus_naur = "xxx1"
        self.pattern = 'abc'
        self.representation = 'rep'


if __name__ == "__main__":
    unittest.main()
