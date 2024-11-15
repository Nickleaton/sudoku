"""TestTemporaryFile."""

import unittest
from pathlib import Path
from src.utils.config import Config
from src.utils.temporary_file import TemporaryFile
import logging

config = Config()


class TestTemporaryFile(unittest.TestCase):
    """Test the TemporaryFile class."""

    def test_create(self):
        """Test creating and using a TemporaryFile."""
        config.reload()
        config.temporary_directory = Path(config.temporary_directory) / Path("non_existing_subdir")
        if config.temporary_directory.exists():
            config.temporary_directory.rmdir()

        try:
            with TemporaryFile() as tf:
                self.assertFalse(tf.name.exists())  # Ensure file doesn't exist initially
                with tf.open(mode='w', encoding='utf-8') as f:
                    f.write('Hello world')  # Write to the temporary file
                self.assertTrue(tf.name.exists())  # Ensure file exists after writing
            self.assertFalse(tf.name.exists())  # Ensure file is removed after closing
            if config.temporary_directory.exists():
                config.temporary_directory.rmdir()  # Clean up directory if needed
        except OSError as e:
            logging.error(f"File operation failed: {e}")
            raise  # Re-raise the exception after logging it
        finally:
            config.reload()

    def test_bad_config(self):
        """Test TemporaryFile with invalid configuration."""
        config.reload()
        try:
            save = config.temporary_directory
            config.temporary_directory = []  # Set invalid config
            # Check that a ValueError is raised when TemporaryFile is used with invalid config
            with self.assertRaises(ValueError):
                _ = TemporaryFile()
            config.temporary_directory = save  # Restore valid config
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
