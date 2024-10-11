import os
from pathlib import Path

# def check_if_writable(file_path: Path) -> bool:
#     """
#     Check if a file is writable, or if the directory allows file creation if it doesn't exist.
#
#     Args:
#         file_path (Path): The path to the file to check.
#
#     Returns:
#         bool: True if the file or directory is writable, False otherwise.
#     """
#     # Check if the file exists and is writable
#     if file_path.exists():
#         return os.access(file_path, os.W_OK)
#     # If the file doesn't exist, check if the parent directory is writable
#     return os.access(file_path.parent, os.W_OK)

def is_writeable_file(file_name: Path) -> bool:
    """
    Check if the given file can be written to.

    If the file does not exist, return True.
    If the file exists and is writable, return True.
    If the file exists but is not writable, return False.

    Args:
        file_name (Path): The name of the file to check.

    Returns:
        bool: True if the file can be written to, False if not.
    """
    # Convert string to Path if necessary
    # Is the file exists and the file is writable
    if not file_name.exists():
        return True  # File doesn't exist, so can be created
    if file_name.is_file() and os.access(file_name, os.W_OK):
        return True  # File exists and is writable

    return False  # File exists but is not writable

def is_readable_file(file_name: Path) -> bool:
    """
    Check if the given file can be read.

    If the file exists and is readable, return True.
    If the file does not exist or is not readable, return False.

    Args:
        file_name (Path): The Path object representing the file to check.

    Returns:
        bool: True if the file can be read, False if not.
    """
    # Check if the file exists and is readable
    if file_name.is_file() and os.access(file_name, os.R_OK):
        return True  # File exists and is readable

    return False  # File does not exist or is not readable