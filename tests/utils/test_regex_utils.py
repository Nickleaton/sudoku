"""TestRegexUtils."""
import unittest

from src.utils.regex_utils import RegexUtils  # Adjust import if needed


class TestRegexUtils(unittest.TestCase):
    """Test the RegexUtils class."""

    def test_strip_names(self):
        """Strip named groups from the regular expression pattern."""
        cases = (
            (r'(?P<word>\w+)-(?P<digit>\d+)', r'(\w+)-(\d+)'),
            (r'(?P<name>[A-Za-z]+) (?P<age>\d+)', r'([A-Za-z]+) (\d+)'),
            (r'(\d+)-(?P<year>\d{4})', r'(\d+)-(\d{4})'),
            (r'(?P<x>[a-z]+)(?P<y>[0-9]+)', r'([a-z]+)([0-9]+)'),
            (r'no_named_groups_here', r'no_named_groups_here'),  # No changes
            (r'(?P<outer>(?P<inner>\d+))', r'((\d+))'),  # Nested groups
            # Extracted patterns
            (r'(?P<minimum>\d)\.\.(?P<maximum>\d\d{0,1})', r'(\d)\.\.(\d\d{0,1})'),
            (r'(?P<row>\d)x(?P<col>\d)', r'(\d)x(\d)'),
            (r'(?P<row>\d)(?P<col>\d)', r'(\d)(\d)'),
            (r'(?P<cycle>[CA])', r'([CA])'),
            (r'(?P<digit>\d)', r'(\d)'),
            (r'(?P<cell>[0-9.lmheofs])', r'([0-9.lmheofs])'),
            (r'(?P<quads>[\d?]{0,4})', r'([\d?]{0,4})'),
            (r'(?P<side>[TLBR])', r'([TLBR])'),
            (r'(?P<row>\d\d{0,1})x(?P<col>\d\d{0,1})', r'(\d\d{0,1})x(\d\d{0,1})'),
            (r'(?P<value>\d+)', r'(\d+)'),
        )

        for pattern, expected in cases:
            with self.subTest(pattern=pattern):
                """Ensure that the named groups are stripped from the pattern."""
                self.assertEqual(RegexUtils.strip_names(pattern), expected)


if __name__ == '__main__':
    unittest.main()
