""" Generate a temporary filename in the temp directory

        with TemporaryFile() as tf:
            with open (tf.name, 'w') as f:
                f.write ("Hello World")

"""
from pathlib import Path
from uuid import uuid4

from src.utils.config import Config

config = Config()


class TemporaryFile:
    """ Generate a temporary file name. Runs in a context """

    def __init__(self):
        """  Create Temporary file

        Use the config temporary directory specified in the config file
        """
        directory = Path(config.temporary_directory)
        directory.mkdir(exist_ok=True)
        u = str(uuid4())
        file_name = Path(u)
        self._name = directory / file_name

    @property
    def name(self) -> Path:
        """ Get the name of the file

        :return: Path
        """
        return self._name

    def __enter__(self):
        """ Handle the context """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """" Handle the context """
        self._name.unlink(missing_ok=True)
