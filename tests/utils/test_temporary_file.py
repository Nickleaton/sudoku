import unittest

from src.utils.temporary_file import TemporaryFile


class TestTemporaryFile(unittest.TestCase):

    def test_create(self):
        with TemporaryFile() as tf:
            self.assertFalse(tf.name.exists())
            with open (tf.name, 'w') as f:
                f.write ('Hello world')
            self.assertTrue(tf.name.exists())
        self.assertFalse(tf.name.exists())


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
