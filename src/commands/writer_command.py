""" Command that takes a command that produces and output string and writes it to a file """
from pathlib import Path

from src.commands.command import Command
from src.commands.simple_command import SimpleCommand


class WriterCommand(Command):
    """ Create a file from the output of a child commmand"""

    def __init__(self, child: SimpleCommand, file_name: Path, output: str):
        """ Create the writer command

        :param child: Simple node that produces an output string
        :param file_name: Path for where to writer the output to
        """
        super().__init__()
        self.child = child
        self.file_name = file_name
        self.output = output

    def execute(self) -> None:
        """ Produce the file """
        self.child.execute()
        self.check_directory(self.file_name)
        with open(self.file_name, 'w') as f:
            f.write(self.child.output[self.output])

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({repr(self.child)}, {repr(str(self.file_name))})"
