"""Functions to handle files."""
import os
from pathlib import Path


def is_writeable_file(file: Path) -> bool:
    """
    Check if the given file can be written to.

    If the file does not exist, return True (it can be created).
    If the file exists and is writable, return True.
    Otherwise, return False.

    Args:
        file (Path): The file path to check.

    Returns:
        bool: True if the file can be written to or created, False if not.
    """
    if not file.exists():
        return True  # File doesn't exist, so it can be created
    return file.is_file() and os.access(file, os.W_OK)


def is_readable_file(file: Path) -> bool:
    """
    Check if the given file can be read.

    If the file exists and is readable, return True.
    Otherwise, return False.

    Args:
        file (Path): The file path to check.

    Returns:
        bool: True if the file can be read, False if not.
    """
    if not file.is_file():
        return False
    return os.access(file, os.R_OK)
