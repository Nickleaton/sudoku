import unittest
from pathlib import Path

from src.utils.config import Config
from src.utils.temporary_file import TemporaryFile

config = Config()


class TestTemporaryFile(unittest.TestCase):

    def test_create(self):
        config.reload()
        config.temporary_directory = Path(config.temporary_directory) / Path("non_existing_subdir")
        if config.temporary_directory.exists():
            config.temporary_directory.rmdir()

        try:
            with TemporaryFile() as tf:
                self.assertFalse(tf.name.exists())
                with tf.open(mode='w', encoding='utf-8') as f:
                    f.write('Hello world')
                self.assertTrue(tf.name.exists())
            self.assertFalse(tf.name.exists())
            if config.temporary_directory.exists():
                config.temporary_directory.rmdir()
        except OSError as e:
            logging.error(f"File operation failed: {e}")
            raise  # Re-raise the exception after logging it
        finally:
            config.reload()

    def test_bad_config(self):
        config.reload()
        try:
            save = config.temporary_directory
            config.temporary_directory = []
            # Check that the ValueError is raised when TemporaryFile is used with invalid config
            with self.assertRaises(ValueError):
                _ = TemporaryFile()
            config.temporary_directory = save
        except ValueError as e:
            logging.error(f"Expected ValueError: {e}")
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            raise  # Re-raise the exception to fail the test if it's not the expected one
        finally:
            config.reload()
            config.reload()


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
