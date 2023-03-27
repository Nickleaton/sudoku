""" Produce output to a file """
import logging
from pathlib import Path

from src.commands.command import Command


class WriterCommand(Command):
    """ Create a file from the output """

    def __init__(self, file_name: Path, reference: str):
        """ Create the writer command

        :param file_name: Path for where to writer the output to
        :param reference: Attribute to write out
        """
        super().__init__()
        self.file_name = file_name
        self.reference = reference

    def execute(self) -> None:
        """ Produce the file """
        logging.info(f"Writing file {self.file_name}")
        self.check_directory(self.file_name)
        with open(self.file_name, 'w') as f:
            f.write(getattr(self, self.reference))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({repr(self.file_name)}, {repr(self.reference)})"
