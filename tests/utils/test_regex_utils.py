import unittest

from src.utils.regex_utils import RegexUtils  # Adjust import if needed


class TestRegexUtils(unittest.TestCase):
    def test_strip_names(self):
        cases = [
            (r'(?P<word>\w+)-(?P<digit>\d+)', r'(\w+)-(\d+)'),
            (r'(?P<name>[A-Za-z]+) (?P<age>\d+)', r'([A-Za-z]+) (\d+)'),
            (r'(\d+)-(?P<year>\d{4})', r'(\d+)-(\d{4})'),
            (r'(?P<x>[a-z]+)(?P<y>[0-9]+)', r'([a-z]+)([0-9]+)'),
            (r'no_named_groups_here', r'no_named_groups_here'),  # No changes
            (r'(?P<outer>(?P<inner>\d+))', r'((\d+))'),  # Nested groups
        ]

        for pattern, expected in cases:
            with self.subTest(pattern=pattern):
                self.assertEqual(RegexUtils.strip_names(pattern), expected)


if __name__ == '__main__':
    unittest.main()
