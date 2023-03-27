""" Command that takes a command that produces and output string and writes it to a file """
from pathlib import Path
from typing import List

from src.commands.simple_command import SimpleCommand


class FileWriterCommand(SimpleCommand):
    """ Create a file from the output of a child commmand"""

    def __init__(self, file_name: Path, values: List[str]):
        """ Create the writer command

        :param file_name: Path for where to writer the output to
        :param values: Dict of strings containing the attributes to dump
        """
        super().__init__()
        self.file_name = file_name
        self.values = values

    def execute(self) -> None:
        super().execute()
        """ Produce the file """
        self.check_directory(self.file_name)
        with open(self.file_name, 'w', encoding="utf-8") as f:
            output = ""
            obj = self.parent
            for v in self.values:
                while "." in v:
                    head, v = v.split(".")
                    obj = getattr(obj, head)
                obj = getattr(obj, v)
                output += obj
            f.write(output)
            f.close()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({repr(self.file_name)}, {repr(self.values)})"
