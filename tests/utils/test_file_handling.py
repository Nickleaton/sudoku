import os
import tempfile
import unittest
from pathlib import Path

from src.utils.file_handling import is_readable_file, is_writeable_file


class TestFilePermissions(unittest.TestCase):

    def test_nonexistent_file(self):
        # Scenario 1: File that doesn't exist
        non_existent_file = Path(tempfile.gettempdir()) / "nonexistent_file.txt"
        self.assertFalse(is_readable_file(non_existent_file))
        self.assertTrue(is_writeable_file(non_existent_file))

    def test_existing_readable_writeable_file(self):
        # Scenario 2: File that exists and is both readable and writeable
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            file_path = Path(temp_file.name)

        try:
            self.assertTrue(is_readable_file(file_path))
            self.assertTrue(is_writeable_file(file_path))
        finally:
            file_path.unlink(missing_ok=True)  # Clean up the temporary file

    def test_existing_readable_not_writeable_file(self):
        # Scenario 3: File that exists, is readable but not writeable
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            file_path = Path(temp_file.name)
        try:
            # Make file read-only
            os.chmod(file_path, 0o444)  # Read-only permissions
            self.assertTrue(is_readable_file(file_path))
            self.assertFalse(is_writeable_file(file_path))
        finally:
            os.chmod(file_path, 0o666)  # Restore write permissions for cleanup
            file_path.unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()
