""" Command that takes a command that produces and output string and writes it to a file """
import logging
from pathlib import Path

from src.commands.command import CommandException
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.utils.file_handling import check_if_writable


class FileWriterCommand(SimpleCommand):
    """ Create a file from the output of a child command"""

    def __init__(self, problem_field: str, file_name: Path):
        """
        Construct a FileWriterCommand

        :param problem_field: The attribute of the problem to write out
        :param file_name: The name of the file to write to
        """
        super().__init__()
        self.file_name: Path = file_name
        self.problem_field: str = problem_field

    def precondition_check(self, problem: Problem) -> None:

        if self.problem_field not in problem:
            raise CommandException(f'{self.__class__.__name__} - {self.problem_field} not in problem')
        if problem[self.problem_field] is None:
            raise CommandException(f'{self.__class__.__name__} - {self.problem_field} is None')
        if self.file_name.exists():
            if not self.file_name.is_file():
                raise CommandException(f'{self.__class__.__name__} - {self.file_name} exists and is not a file')

            if not check_if_writable(self.file_name):
                raise CommandException(f'{self.__class__.__name__} - {self.file_name} is not writeable')

    def execute(self, problem: Problem) -> None:
        super().execute(problem)
        """ Produce the file """
        self.file_name.parent.mkdir(exist_ok=True)
        logging.info(f"Writing file {self.file_name}")
        with open(self.file_name, 'w', encoding="utf-8") as f:
            f.write(problem[self.problem_field])
            f.close()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({repr(self.problem_field)}, {repr(self.file_name)})"
