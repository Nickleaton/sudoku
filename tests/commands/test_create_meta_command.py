import unittest

from src.commands.create_meta_command import CreateMetaCommand
from src.commands.load_config_command import LoadConfigCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestCreateMetaCommand(TestSimpleCommand):

    def setUp(self) -> None:
        super().setUp()
        requirements = LoadConfigCommand(self.path)
        requirements.execute(self.problem)
        self.command = CreateMetaCommand()

    def test_command(self):
        self.assertIn('config', self.problem)
        self.assertNotIn('meta', self.problem)
        self.command.execute(self.problem)
        self.assertIn('meta', self.problem)

    @property
    def representation(self) -> str:
        return r"CreateMetaCommand('config', 'meta')"

    def test_repr(self):
        self.assertEqual(self.representation, repr(self.command))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
