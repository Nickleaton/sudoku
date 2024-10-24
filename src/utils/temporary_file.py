"""Generate a temporary filename in the temp directory.

Example:
    ```python
    with TemporaryFile() as tf:
        with open(tf.name, 'w') as f:
            f.write("Hello World")
    ```
"""
import logging
from pathlib import Path
from uuid import uuid4

from src.utils.config import Config

config = Config()


class TemporaryFile:
    """Generate a temporary file name. Runs in a context."""

    def __init__(self):
        """Create a TemporaryFile instance.

        This constructor creates a temporary file in the directory specified
        in the configuration file. If the directory does not exist, it will
        be created.

        Raises:
            OSError: If the directory cannot be created.
        """
        directory: Path = Path(config.temporary_directory)
        if not directory.exists():
            logging.info(f"Creating directory {directory}")
            directory.mkdir(parents=True)
        file_name: Path = Path(str(uuid4()))
        self._name: Path = directory / file_name

    @property
    def name(self) -> Path:
        """Get the name of the temporary file.

        Returns:
            Path: The path of the temporary file.
        """
        return self._name

    def __enter__(self):
        """Enter the runtime context related to this object.

        Returns:
            TemporaryFile: The TemporaryFile instance itself.
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit the runtime context and remove the temporary file.

        This method is called when leaving the context manager. It
        deletes the temporary file if it exists.

        Args:
            exc_type (type): The exception type if an exception was raised.
            exc_val (Exception): The exception instance if an exception was raised.
            exc_tb (TracebackType): The traceback object if an exception was raised.
        """
        self._name.unlink(missing_ok=True)
