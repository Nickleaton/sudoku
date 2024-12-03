import unittest
from pathlib import Path

from src.commands.command import Command, CommandException
from src.commands.key_type import KeyType
from src.commands.parameter_value_type import ParameterValueType
from src.commands.problem import Problem


class TestCommand(unittest.TestCase):
    """Test suite for the Command class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        self.command = Command()
        self.problem = Problem()
        self.empty_problem = Problem()
        self.config_file: Path = Path(r'problems\easy\problem001.yaml')
        self.missing_file: Path = Path(r'output\tests\nonexistent.txt')
        self.readable_file: Path = Path(r'output\tests\output.txt')
        self.writable_file: Path = Path(r'output\tests\output.txt')
        self.readable_file.parent.mkdir(parents=True, exist_ok=True)
        with self.readable_file.open('w') as f:
            f.write("Hello World")
        if self.writable_file.exists():
            self.writable_file.unlink()
        self.representation = f"{self.command.__class__.__name__}()"

    def tearDown(self):
        """Clean up the test environment."""
        if self.readable_file.exists():
            self.readable_file.unlink()
        if self.writable_file.exists():
            self.writable_file.unlink()

    def test_command_name(self):
        """Test the name property of the Command class."""
        if self.command is None:
            return
        expected_name: str = "Command" \
            if self.__class__.__name__ == 'TestCommand' \
            else self.__class__.__name__.replace("Test", "").replace("Command", "")
        self.assertEqual(self.command.name, expected_name)

    def test_command_execute(self):
        """Test the execute method of the Command class."""
        self.command.execute(self.problem)

    def test_set_parameters(self):
        """Test the set_parameters method of the Command class."""
        # Define parameters to be set in the problem
        self.command.parameters = [
            ParameterValueType("param1", "test", str),
            ParameterValueType("param2", 99, int),
            ParameterValueType("param3", Path("test.txt"), Path),
        ]

        # Ensure the problem does not initially contain these keys
        for param in self.command.parameters:
            self.assertNotIn(param.key, self.problem)

        # Call set_parameters
        self.command.set_parameters(self.problem)

        # Check that parameters were set with their default values
        self.assertEqual(self.problem["param1"], "test")
        self.assertEqual(self.problem["param2"], 99)
        self.assertEqual(self.problem["param3"], Path("test.txt"))

    def test_validate_parameters_exists(self):
        """Test the validate_parameters method for parameters that must exist."""
        # Define parameters expected in the problem
        parameters = [
            ParameterValueType("param1", "text", str),
            ParameterValueType("param2", 99, int),
        ]

        # Populate the problem with valid parameters
        self.problem["param1"] = "some text"
        self.problem["param2"] = 42

        # Should not raise an exception
        try:
            self.command.validate_parameters(self.problem, parameters, check_exists=True)
        except CommandException as e:
            self.fail(f"validate_parameters (exists) raised CommandException unexpectedly: {e}")

        # Test with a missing key
        del self.problem["param1"]  # Remove one key
        with self.assertRaises(CommandException) as context:
            self.command.validate_parameters(self.problem, parameters, check_exists=True)
        self.assertIn("'param1' is missing from the problem", str(context.exception))

        # Test with the wrong type
        self.problem["param1"] = 123  # Wrong type
        with self.assertRaises(CommandException) as context:
            self.command.validate_parameters(self.problem, parameters, check_exists=True)
        self.assertIn("'param1' is of the wrong type", str(context.exception))

    def test_validate_parameters_not_exists(self):
        """Test the validate_parameters method for parameters that must not exist."""
        # Define parameters that should not exist in the problem
        parameters = [
            ParameterValueType("param1", "text", str),
            ParameterValueType("param2", 99, int),
        ]

        # Ensure the problem does not contain these keys
        self.assertNotIn("param1", self.problem)
        self.assertNotIn("param2", self.problem)

        # Should not raise an exception
        try:
            self.command.validate_parameters(self.problem, parameters, check_exists=False)
        except CommandException as e:
            self.fail(f"validate_parameters (not exists) raised CommandException unexpectedly: {e}")

        # Add one of the keys to the problem
        self.problem["param1"] = "already exists"
        with self.assertRaises(CommandException) as context:
            self.command.validate_parameters(self.problem, parameters, check_exists=False)
        self.assertIn("'param1' already exists in the problem", str(context.exception))

    def test_validate_values_exists(self):
        """Test the validate_values method for values that must exist."""
        # Define expected values in the problem
        values = [
            KeyType("value1", str),
            KeyType("value2", int),
        ]

        # Populate the problem with valid values
        self.problem["value1"] = "some text"
        self.problem["value2"] = 42

        # Should not raise an exception
        try:
            self.command.validate_values(self.problem, values, check_exists=True)
        except CommandException as e:
            self.fail(f"validate_values (exists) raised CommandException unexpectedly: {e}")

        # Test with a missing key
        del self.problem["value1"]  # Remove one key
        with self.assertRaises(CommandException) as context:
            self.command.validate_values(self.problem, values, check_exists=True)
        self.assertIn("'value1' is missing from the problem", str(context.exception))

        # Test with the wrong type
        self.problem["value1"] = 123  # Wrong type
        with self.assertRaises(CommandException) as context:
            self.command.validate_values(self.problem, values, check_exists=True)
        self.assertIn("'value1' is of the wrong type", str(context.exception))

    def test_validate_values_not_exists(self):
        """Test the validate_values method for values that must not exist."""
        # Define expected output values
        values = [
            KeyType("value1", str),
            KeyType("value2", int),
        ]

        # Ensure the problem does not contain these keys
        self.assertNotIn("value1", self.problem)
        self.assertNotIn("value2", self.problem)

        # Should not raise an exception
        try:
            self.command.validate_values(self.problem, values, check_exists=False)
        except CommandException as e:
            self.fail(f"validate_values (not exists) raised CommandException unexpectedly: {e}")

        # Add one of the keys to the problem
        self.problem["value1"] = "already exists"
        with self.assertRaises(CommandException) as context:
            self.command.validate_values(self.problem, values, check_exists=False)
        self.assertIn("'value1' already exists in the problem", str(context.exception))

    def test_repr(self):
        """Test the __repr__ method of the Command class."""
        if self.command is None:
            return
        self.assertEqual(self.representation, repr(self.command))

    def test_parameter_type_mismatch(self):
        """Test if a TypeError is raised when a parameter type is mismatched."""
        with self.assertRaises(TypeError):
            ParameterValueType("param1", "string_value", int)

    def test_command_exception(self):
        """Test if CommandException raises with the correct message."""
        with self.assertRaises(CommandException) as context:
            raise CommandException("parameter1")
        self.assertEqual(str(context.exception), "Error in parameter1")


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
