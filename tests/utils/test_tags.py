import unittest

from src.utils.tags import Tags  # Assuming the Tags class is defined in a module named `tags`


class TestTags(unittest.TestCase):
    def setUp(self):
        # Prepare test data
        self.dict1 = {'Key1': 'value1', 'Key2': 'value2'}
        self.dict2 = {'key1': 'value1', 'key2': 'value2'}
        self.dict3 = {'KEY1': 'value1', 'KEY3': 'value3'}

        self.tags1 = Tags(self.dict1)
        self.tags2 = Tags(self.dict2)
        self.tags3 = Tags(self.dict3)

    def test_keys_are_lowercase(self):
        # Ensure keys are converted to lowercase
        self.assertEqual(self.tags1.to_dict(), {'key1': 'value1', 'key2': 'value2'})
        self.assertEqual(self.tags3.to_dict(), {'key1': 'value1', 'key3': 'value3'})

    def test_equality(self):
        # Test equality operator
        self.assertTrue(self.tags1 == self.tags2)
        self.assertFalse(self.tags1 == self.tags3)

    def test_access_via_dot(self):
        # Ensure dot notation works
        self.assertEqual(self.tags1.key1, 'value1')
        self.assertEqual(self.tags3.key3, 'value3')

    def test_invalid_access(self):
        # Test access of invalid keys
        with self.assertRaises(AttributeError):
            _ = self.tags1.invalid_key


if __name__ == '__main__':
    unittest.main()
