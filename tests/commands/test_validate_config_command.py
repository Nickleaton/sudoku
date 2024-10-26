import unittest

from src.commands.problem import Problem
from src.commands.validate_config_command import ValidateConfigCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestValidateConfigCommand(TestSimpleCommand):

    def setUp(self) -> None:
        super().setUp()
        self.command = ValidateConfigCommand(self.path)
        self.problem = Problem()

    @property
    def representation(self) -> str:
        return r"ValidateConfigCommand('problems\\easy\\problem001.yaml', 'config_validation')"

    def test_repr(self):
        self.assertEqual(self.representation, repr(self.command))

    def test_execute(self):
        self.command.execute(self.problem)
        print(self.problem.config_validation)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
