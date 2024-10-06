import logging

from src.commands.command import CommandException
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand


class CreateRulesCommand(SimpleCommand):

    def __init__(self):
        super().__init__()

    def execute(self, problem: Problem) -> None:
        if problem.constraints.sorted_unique_rules is None:
            logging.error("Sorted unique rules is None")  # pragma: no cover
        else:
            problem.rules = [{'name': rule.name, 'text': rule.text} for rule in problem.constraints.sorted_unique_rules]

    def precondition_check(self, problem: Problem) -> None:
        if problem.config is None:
            raise CommandException('config')
        if problem.board is None:
            raise CommandException('board')
        if problem.constraints is None:
            raise CommandException('constraints')