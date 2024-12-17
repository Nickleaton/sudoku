import unittest
from xml.dom.minidom import parseString

from src.utils.pretty_xml import PrettyXML  # Assume PrettyXML is in a file named pretty_xml.py


class TestPrettyXML(unittest.TestCase):
    """Test cases for the PrettyXML class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        self.raw_xml = '<root><child>Test</child></root>'
        self.invalid_xml = '<root><child>Invalid</root>'
        self.pretty_xml = PrettyXML()

    def test_set_raw_string(self) -> None:
        """Test setting the raw XML string updates the DOM and pretty string."""
        self.pretty_xml.raw_string = self.raw_xml

        # Check raw string
        self.assertEqual(self.pretty_xml.raw_string, self.raw_xml)

        # Check DOM object
        self.assertIsNotNone(self.pretty_xml.dom)

        # Check pretty-printed output
        expected_pretty = '<?xml version="1.0" ?>\n<root>\n  <child>Test</child>\n</root>\n'
        self.assertEqual(self.pretty_xml.pretty_string, expected_pretty)

    def test_set_invalid_raw_string(self) -> None:
        """Test setting an invalid raw XML string raises ValueError."""
        with self.assertRaises(ValueError):
            self.pretty_xml.raw_string = self.invalid_xml

    def test_set_dom(self) -> None:
        """Test setting the DOM updates the raw string and pretty string."""
        dom = parseString('<data><item>42</item></data>')
        self.pretty_xml.dom = dom

        # Check DOM object
        self.assertEqual(self.pretty_xml.dom.toxml(), dom.toxml())

        # Check raw string
        expected_raw = '<?xml version="1.0" ?><data><item>42</item></data>'
        self.assertEqual(self.pretty_xml.raw_string, expected_raw)

        # Check pretty-printed output
        expected_pretty = '<?xml version="1.0" ?>\n<data>\n  <item>42</item>\n</data>\n'
        self.assertEqual(self.pretty_xml.pretty_string, expected_pretty)

    def test_pretty_string_after_raw_update(self) -> None:
        """Test that pretty_string is updated when raw_string changes."""
        new_raw = '<a><b>123</b></a>'
        self.pretty_xml.raw_string = new_raw

        expected_pretty = '<?xml version="1.0" ?>\n<a>\n  <b>123</b>\n</a>\n'
        self.assertEqual(self.pretty_xml.pretty_string, expected_pretty)

    def test_pretty_string_after_dom_update(self) -> None:
        """Test that pretty_string is updated when the DOM changes."""
        new_dom = parseString('<x><y>456</y></x>')
        self.pretty_xml.dom = new_dom

        expected_pretty = '<?xml version="1.0" ?>\n<x>\n  <y>456</y>\n</x>\n'
        self.assertEqual(self.pretty_xml.pretty_string, expected_pretty)


if __name__ == '__main__':
    unittest.main()
