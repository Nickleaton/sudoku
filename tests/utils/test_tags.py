import unittest

from src.utils.tags import Tags  # Assuming the Tags class is defined in a file named `tags.py`


class TestTags(unittest.TestCase):
    def setUp(self):
        # Prepare test data
        self.dict1 = {'Key1': 'value1', 'Key2': 'value2'}
        self.dict2 = {'Key1': 'value1', 'Key2': 'value2'}
        self.dict3 = {'Key1': 'value1', 'Key3': 'value3'}

        self.tags1 = Tags(self.dict1)
        self.tags2 = Tags(self.dict2)
        self.tags3 = Tags(self.dict3)

    def test_initialization(self):
        # Ensure data is initialized correctly
        self.assertEqual(self.tags1.to_dict(), {'Key1': 'value1', 'Key2': 'value2'})
        self.assertEqual(self.tags3.to_dict(), {'Key1': 'value1', 'Key3': 'value3'})

    def test_equality(self):
        # Test equality operator
        self.assertTrue(self.tags1 == self.tags2)  # Equal
        self.assertFalse(self.tags1 == self.tags3)  # Not equal
        self.assertFalse(self.tags1 == 'Not a Tags object')  # Comparing with non-Tags object

    def test_access_via_dot(self):
        # Ensure dot notation works
        self.assertEqual(self.tags1.Key1, 'value1')
        self.assertEqual(self.tags3.Key3, 'value3')


if __name__ == '__main__':
    unittest.main()
