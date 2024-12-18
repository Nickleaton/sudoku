import unittest

from src.utils.pretty_print_xml import pretty_print_xml


class TestPrettyPrintXML(unittest.TestCase):
    def setUp(self):
        """Set up valid and invalid XML strings for testing."""
        self.valid_xml = '<root><child1>value1</child1><child2>value2</child2></root>'
        self.expected_output = (
            '<root>\n'
            '  <child1>value1</child1>\n'
            '  <child2>value2</child2>\n'
            '</root>'
        )
        self.invalid_xml = '<root><child1>value1</child2></root>'

    def test_pretty_print_valid_xml(self):
        """Test pretty printing of a valid XML string."""
        result = pretty_print_xml(self.valid_xml)
        self.assertEqual(result, self.expected_output)

    def test_pretty_print_invalid_xml(self):
        """Test handling of an invalid XML string."""
        result = pretty_print_xml(self.invalid_xml)
        self.assertTrue(result.startswith('Error parsing XML:'))
        self.assertIn('mismatched tag', result)

    def test_empty_xml_string(self):
        """Test handling of an empty string as input."""
        result = pretty_print_xml('')
        self.assertTrue(result.startswith('Error parsing XML:'))

    def test_single_element(self):
        """Test pretty printing of a single-element XML string."""
        single_element = '<root></root>'
        expected = '<root/>'
        result = pretty_print_xml(single_element)
        self.assertEqual(result, expected)

    def test_nested_xml(self):
        """Test pretty printing of a nested XML structure."""
        nested_xml = '<root><parent><child>value</child></parent></root>'
        expected = (
            '<root>\n'
            '  <parent>\n'
            '    <child>value</child>\n'
            '  </parent>\n'
            '</root>'
        )
        result = pretty_print_xml(nested_xml)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
