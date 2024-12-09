"""TestFileHandling."""
import tempfile
import unittest
from pathlib import Path

from src.utils.file_handling import is_readable_file, is_writeable_file


class TestFilePermissions(unittest.TestCase):
    """Test file_path read and write permissions."""

    def test_nonexistent_file(self):
        """Test non-existent file_path."""
        # Scenario 1: File that doesn't exist
        non_existent_file = Path(tempfile.gettempdir()) / "nonexistent_file.txt"
        self.assertFalse(is_readable_file(non_existent_file))
        self.assertTrue(is_writeable_file(non_existent_file))

    def test_existing_readable_writeable_file(self):
        """Test an existing file_path that is both readable and writable."""
        # Scenario 2: File that exists and is both readable and writable
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            file_path = Path(temp_file.name)

        try:
            self.assertTrue(is_readable_file(file_path))
            self.assertTrue(is_writeable_file(file_path))
        finally:
            file_path.unlink(missing_ok=True)  # Clean up the temporary file_path

    def test_existing_readable_not_writeable_file(self):
        """Test an existing file_path that is readable but not writable."""
        # Scenario 3: File that exists, is readable but not writable
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            file_path = Path(temp_file.name)
        try:
            # Make file_path read-only
            file_path.chmod(0o444)  # Read-only permissions
            self.assertTrue(is_readable_file(file_path))
            self.assertFalse(is_writeable_file(file_path))
        finally:
            file_path.chmod(0o666)  # Restore write permissions for cleanup
            file_path.unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()
