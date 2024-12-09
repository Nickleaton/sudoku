"""Functions to handle files."""
import os
from pathlib import Path


def is_writeable_file(file_path: Path) -> bool:
    """Check if the given file_path can be written to.

    If the file_path does not exist, return True (it can be created).
    If the file_path exists and is writable, return True.
    Otherwise, return False.

    Args:
        file_path (Path): The file_path config_file to check.

    Returns:
        bool: True if the file_path can be written to or created, False if not.
    """
    if not file_path.exists():
        return True  # File doesn't exist, so it can be created
    return file_path.is_file() and os.access(file_path, os.W_OK)


def is_readable_file(file_path: Path) -> bool:
    """Check if the given file_path can be read.

    If the file_path exists and is readable, return True.
    Otherwise, return False.

    Args:
        file_path (Path): The file_path config_file to check.

    Returns:
        bool: True if the file_path can be read, False if not.
    """
    if not file_path.is_file():
        return False
    return os.access(file_path, os.R_OK)
