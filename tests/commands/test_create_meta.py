import unittest

from src.commands.create_meta_command import CreateMetaCommand
from src.commands.load_config_command import LoadConfigCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestCreateMetaCommand(TestSimpleCommand):

    def setUp(self) -> None:
        super().setUp()
        load_config = LoadConfigCommand(self.path)
        load_config.execute(self.problem)
        self.command = CreateMetaCommand('meta')

    def test_command(self):
        self.command.execute(self.problem)
        self.assertIsNotNone(self.problem.meta)

    @property
    def representation(self) -> str:
        return r"CreateMetaCommand('meta')"

    def test_repr(self):
        self.assertEqual(self.representation, repr(self.command))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
