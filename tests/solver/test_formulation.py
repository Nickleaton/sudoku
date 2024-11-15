"""Test Formulations for linear programming constraints."""
import inspect
import unittest
from pathlib import Path
from typing import List, Dict, ClassVar

from pulp import LpVariable, LpInteger, LpProblem, LpMinimize, getSolver, LpContinuous, LpSolver

from src.solvers.formulations import Formulations


class TestFormulation(unittest.TestCase):
    """Test various formulations in linear programming problems."""

    logs: ClassVar[Dict[str, int]] = {}
    lp_files: ClassVar[Dict[str, int]] = {}

    def setUp(self) -> None:
        """Initialize test environment by creating necessary directories."""
        # Set up directories for log and LP files
        self.base = Path("output/formulations")
        self.log_path = self.base / Path("logs")
        self.lp_path = self.base / Path("lp")
        self.log_path.mkdir(exist_ok=True, parents=True)
        self.lp_path.mkdir(exist_ok=True, parents=True)

    def get_application(self, name: str) -> LpSolver:
        """Retrieve an LpSolver instance based on the solver name.

        Args:
            name (str): The name of the solver.

        Returns:
            LpSolver: An instance of the LpSolver class.
        """
        if name not in TestFormulation.logs:
            TestFormulation.logs[name] = 0
        else:
            TestFormulation.logs[name] += 1
        log_file_name = Path(f"{name}_{TestFormulation.logs[name]}.log")
        log_file = self.log_path / log_file_name
        return getSolver('PULP_CBC_CMD', logPath=str(log_file), msg=False, timeLimit=60)

    def get_lp_filename(self, name: str) -> Path:
        """Generate and return the filename for an LP file based on the provided name.

        Args:
            name (str): The base name of the LP file.

        Returns:
            Path: The full path of the LP file.
        """
        if name not in TestFormulation.lp_files:
            TestFormulation.lp_files[name] = 0
        else:
            TestFormulation.lp_files[name] += 1
        file_name = Path(f"{name}_{TestFormulation.lp_files[name]}.lp")
        return self.lp_path / file_name

    def absolute_int(self, v1: int, v2: int, expected: int) -> None:
        """Test the absolute difference between two integers using linear programming.

        Args:
            v1 (int): The first integer value.
            v2 (int): The second integer value.
            expected (int): The expected result of the absolute difference.

        Returns:
            None
        """
        model = LpProblem("absolute_int", LpMinimize)
        x = LpVariable("minimum", 0, 9, LpInteger)
        x1 = LpVariable("x1", 1, 9, LpInteger)
        x2 = LpVariable("x2", 1, 9, LpInteger)

        model += x1 == v1
        model += x2 == v2
        model += x == Formulations.abs(model, x1, x2, 9)
        model.writeLP(str(self.get_lp_filename(inspect.currentframe().f_code.co_name)))
        model.solve(self.get_application(inspect.currentframe().f_code.co_name))
        self.assertEqual(expected, x.varValue)

    def test_absolute_int(self) -> None:
        """Test absolute difference for integer values.

        Returns:
            None
        """
        self.absolute_int(3, 9, 6)
        self.absolute_int(5, 3, 2)
        self.absolute_int(1, 1, 0)

    def absolute_float(self, v1: float, v2: float, expected: float) -> None:
        """Test the absolute difference between two floating-point numbers using linear programming.

        Args:
            v1 (float): The first floating-point value.
            v2 (float): The second floating-point value.
            expected (float): The expected result of the absolute difference.

        Returns:
            None
        """
        model = LpProblem("absolute_float", LpMinimize)
        x = LpVariable("minimum", 0, 9, LpContinuous)
        x1 = LpVariable("x1", 1, 9, LpContinuous)
        x2 = LpVariable("x2", 1, 9, LpContinuous)

        model += x1 == v1
        model += x2 == v2
        model += x == Formulations.abs(model, x1, x2, 9)
        model.writeLP(str(self.get_lp_filename(inspect.currentframe().f_code.co_name)))
        model.solve(self.get_application(inspect.currentframe().f_code.co_name))
        self.assertEqual(expected, x.varValue)

    def test_absolute_float(self) -> None:
        """Test absolute difference for floating-point values.

        Returns:
            None
        """
        self.absolute_float(3.0, 9.0, 6.0)
        self.absolute_float(5.0, 3.0, 2.0)
        self.absolute_float(1.0, 1.0, 0.0)
        self.absolute_float(1.5, 2.8, 1.3)
        self.absolute_float(4.5, 2.8, 1.7)

    def minimum(self, values: List[int], expected: int) -> None:
        """Test the minimum value of a list using linear programming.

        Args:
            values (List[int]): A list of integer values to find the minimum of.
            expected (int): The expected minimum value.

        Returns:
            None
        """
        model = LpProblem("minimum", LpMinimize)
        variables: List[LpVariable] = []
        for i, value in enumerate(values):
            x = LpVariable(f"x{i}", 1, 9, LpInteger)
            model += x == value
            variables.append(x)

        mini = Formulations.minimum(model, variables, 1, 9)
        model.writeLP(str(self.get_lp_filename(inspect.currentframe().f_code.co_name)))
        model.solve(self.get_application(inspect.currentframe().f_code.co_name))
        self.assertEqual(expected, mini.varValue)

    def test_minimum(self) -> None:
        """Test minimum value for a list of integers.

        Returns:
            None
        """
        self.minimum([2, 2, 2], 2)
        self.minimum([1, 2, 3], 1)
        self.minimum([3, 2, 1], 1)

    def maximum(self, values: List[int], expected: int) -> None:
        """Test the maximum value of a list using linear programming.

        Args:
            values (List[int]): A list of integer values to find the maximum of.
            expected (int): The expected maximum value.

        Returns:
            None
        """
        model = LpProblem("maximum", LpMinimize)
        variables: List[LpVariable] = []
        for i, value in enumerate(values):
            x = LpVariable(f"x{i}", 1, 9, LpInteger)
            model += x == value
            variables.append(x)

        maxi = Formulations.maximum(model, variables, 1, 9)
        model.writeLP(str(self.get_lp_filename(inspect.currentframe().f_code.co_name)))
        model.solve(self.get_application(inspect.currentframe().f_code.co_name))
        self.assertEqual(expected, maxi.varValue)

    def test_maximum(self) -> None:
        """Test maximum value for a list of integers.

        Returns:
            None
        """
        self.maximum([1, 2, 3], 3)
        self.maximum([3, 2, 1], 3)
        self.maximum([2, 2, 2], 2)

    def logical_not(self, value: int, expected: int) -> None:
        """Test logical NOT operation for binary values.

        Args:
            value (int): The binary value to be negated.
            expected (int): The expected result of the logical NOT operation.

        Returns:
            None
        """
        model = LpProblem("logical_not", LpMinimize)
        x = LpVariable("x", 0, 1, LpInteger)
        model += x == value
        y = Formulations.logical_not(model, x)
        model.writeLP(str(self.get_lp_filename(inspect.currentframe().f_code.co_name)))
        model.solve(self.get_application(inspect.currentframe().f_code.co_name))
        self.assertEqual(expected, y.varValue)

    def test_logical_not(self):
        """Test logical NOT operation for binary values.

        Returns:
            None
        """
        self.logical_not(1, 0)
        self.logical_not(0, 1)

    def logical_or(self, value1: int, value2: int, expected: int) -> None:
        """Test logical OR operation for binary values.

        Args:
            value1 (int): The first binary value.
            value2 (int): The second binary value.
            expected (int): The expected result of the logical OR operation.

        Returns:
            None
        """
        model = LpProblem("logical_or", LpMinimize)
        x1 = LpVariable("x1", 0, 1, LpInteger)
        x2 = LpVariable("x2", 0, 1, LpInteger)
        model += x1 == value1
        model += x2 == value2
        y = Formulations.logical_or(model, [x1, x2])
        model.writeLP(str(self.get_lp_filename(inspect.currentframe().f_code.co_name)))
        model.solve(self.get_application(inspect.currentframe().f_code.co_name))
        self.assertEqual(expected, y.varValue)

    def test_logical_or(self):
        """Test logical OR operation for binary values.

        Returns:
            None
        """
        self.logical_or(1, 0, 1)
        self.logical_or(0, 1, 1)
        self.logical_or(0, 0, 0)
        self.logical_or(0, 1, 1)
        self.logical_or(1, 0, 1)
        self.logical_or(1, 1, 1)

    def logical_and(self, value1: int, value2: int, expected: int) -> None:
        """Test the logical AND operation between two binary values.

        Args:
            value1 (int): The first binary value.
            value2 (int): The second binary value.
            expected (int): The expected result of the logical AND operation.

        Returns:
            None
        """
        model = LpProblem("logical_and", LpMinimize)
        x1 = LpVariable("x1", 0, 1, LpInteger)
        x2 = LpVariable("x2", 0, 1, LpInteger)
        model += x1 == value1
        model += x2 == value2
        y = Formulations.logical_and(model, [x1, x2])
        model.writeLP(str(self.get_lp_filename(inspect.currentframe().f_code.co_name)))
        model.solve(self.get_application(inspect.currentframe().f_code.co_name))
        self.assertEqual(expected, y.varValue)

    def test_logical_and(self):
        """Tests the logical_and function with various input combinations.

        The test cases cover all possible combinations of two binary inputs,
        ensuring the function behaves correctly for all scenarios.
        """
        self.logical_and(0, 0, 0)
        self.logical_and(0, 1, 0)
        self.logical_and(1, 0, 0)
        self.logical_and(1, 1, 1)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
