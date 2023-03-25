""" Command base class

Commands are used to do the actual work.
Based on the Command pattern from the Gang of Four book

https://en.wikipedia.org/wiki/Command_pattern
"""
import logging
from pathlib import Path
from typing import Optional


class Command:
    """ Base class for all commands """

    def __init__(self):
        """ Command base class"""
        pass

    @property
    def name(self) -> str:
        """ Get the name of the class in a nice form"""
        if self.__class__.__name__ == 'Command':
            return self.__class__.__name__
        return self.__class__.__name__.replace("Command", "")

    def execute(self) -> None:
        """" Execute the command """
        logging.info(f"{self.__class__.__name__} process")

    #
    # def write(self) -> None:
    #     """ persist the output to output_filename"""
    #     logging.info(f"Writing output to {self.output_filename.name}")
    @staticmethod
    def check_directory(file_name: Path) -> None:
        """ Utility function to create the directory for file_name if it doesn't exist

        :param file_name: Path to the file
        """
        assert file_name is not None
        if not file_name.parent.exists():  # pragma: no cover
            logging.info(f"Creating directory {file_name.parent.name}")
            file_name.parent.mkdir()

    def __repr__(self):
        return f"{self.__class__.__name__}()"
