"""Generate a temporary filename in the temp directory."""
import logging
from pathlib import Path
from types import TracebackType
from typing import Type
from uuid import uuid4

from src.utils.config import Config

config = Config()


class TemporaryFile:
    """Generate a temporary file name. Runs in a context."""

    def __init__(self) -> None:
        """Create a TemporaryFile instance.

        This constructor creates a temporary file in the directory specified
        in the configuration file. If the directory does not exist, it will
        be created.

        Raises:
            OSError: If the directory cannot be created.

        Example:
            with TemporaryFile() as tf:
                with open(tf.name, 'w') as f:
                    f.write("Hello World")
        """
        if not isinstance(config.temporary_directory, (str, Path)):
            raise ValueError("Temporary directory must be a valid config_file string or Path object")

        directory: Path = config.temporary_directory if isinstance(config.temporary_directory, Path) else Path(
            config.temporary_directory)

        if not directory.exists():
            logging.info(f"Creating directory {directory}")
            directory.mkdir(parents=True)

        file_name: str = f"{uuid4()}.tmp"  # Add a ".tmp" extension for clarity
        self._path: Path = directory / file_name

    @property
    def path(self) -> Path:
        """Get the config_file of the temporary file.

        Returns:
            Path: The config_file of the temporary file.
        """
        return self._path

    def __enter__(self) -> 'TemporaryFile':
        """Enter the runtime context related to this object.

        Returns:
            TemporaryFile: The TemporaryFile instance itself.
        """
        return self

    def __exit__(self,
                 _exc_type: Type[BaseException] | None,
                 _exc_val: BaseException | None,
                 _exc_tb: TracebackType | None
                 ) -> None:
        """Exit the runtime context and remove the temporary file.

        This method is called when leaving the context manager. It
        deletes the temporary file if it exists.

        Args:
            exc_type (type | None): The exception type if an exception was raised.
            exc_val (Exception | None): The exception instance if an exception was raised.
            exc_tb (TracebackType | None): The traceback object if an exception was raised.
        """
        self._path.unlink(missing_ok=True)
