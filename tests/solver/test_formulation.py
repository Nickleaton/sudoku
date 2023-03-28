import inspect
import unittest
from pathlib import Path
from typing import List

from pulp import LpVariable, LpInteger, LpProblem, LpMinimize, getSolver, LpContinuous, LpSolver

from src.solvers.formulations import Formulations


class TestFormulation(unittest.TestCase):

    def setUp(self) -> None:
        self.base = Path("output/formulations")
        self.log_path = self.base / Path("logs")
        self.lp_path = self.base / Path("lp")
        self.log_path.mkdir(exist_ok=True)
        self.lp_path.mkdir(exist_ok=True)

    def get_application(self, name: str) -> LpSolver:
        log_file = self.log_path / Path(name + ".log")
        return getSolver('PULP_CBC_CMD', logPath=str(log_file), msg=False, timeLimit=60)

    def get_lp_filename(self) -> Path:
        return self.lp_path / Path(inspect.stack()[1][3] + ".lp")

    def absolute_int(self, v1: int, v2: int, expected: int) -> None:
        model = LpProblem("absolute_int", LpMinimize)
        x = LpVariable("minimum", 0, 9, LpInteger)
        x1 = LpVariable("x1", 1, 9, LpInteger)
        x2 = LpVariable("x2", 1, 9, LpInteger)

        model += x1 == v1
        model += x2 == v2
        model += x == Formulations.abs(model, x1, x2, 9)
        model.writeLP(str(self.get_lp_filename()))
        model.solve(self.get_application('absolute'))
        self.assertEqual(expected, x.varValue)

    def test_absolute_int(self) -> None:
        self.absolute_int(3, 9, 6)
        self.absolute_int(5, 3, 2)
        self.absolute_int(1, 1, 0)

    def absolute_float(self, v1: float, v2: float, expected: float) -> None:
        model = LpProblem("absolute_float", LpMinimize)
        x = LpVariable("minimum", 0, 9, LpContinuous)
        x1 = LpVariable("x1", 1, 9, LpContinuous)
        x2 = LpVariable("x2", 1, 9, LpContinuous)

        model += x1 == v1
        model += x2 == v2
        model += x == Formulations.abs(model, x1, x2, 9)
        model.writeLP(str(self.get_lp_filename()))
        model.solve(self.get_application('absolute'))
        self.assertEqual(expected, x.varValue)

    def test_absolute_float(self) -> None:
        self.absolute_float(3.0, 9.0, 6.0)
        self.absolute_float(5.0, 3.0, 2.0)
        self.absolute_float(1.0, 1.0, 0.0)
        self.absolute_float(1.5, 2.8, 1.3)
        self.absolute_float(4.5, 2.8, 1.7)

    def minimum(self, values: List[int], expected: int) -> None:
        model = LpProblem("minimum", LpMinimize)
        variables: List[LpVariable] = []
        for i, value in enumerate(values):
            x = LpVariable(f"x{i}", 1, 9, LpInteger)
            model += x == value
            variables.append(x)

        mini = Formulations.minimum(model, variables, 1, 9)
        model.writeLP(str(self.get_lp_filename()))
        model.solve(self.get_application('minimum'))
        self.assertEqual(expected, mini.varValue)

    def test_minimum(self) -> None:
        self.minimum([2, 2, 2], 2)
        self.minimum([1, 2, 3], 1)
        self.minimum([3, 2, 1], 1)

    def maximum(self, values: List[int], expected: int) -> None:
        model = LpProblem("maximum", LpMinimize)
        variables: List[LpVariable] = []
        for i, value in enumerate(values):
            x = LpVariable(f"x{i}", 1, 9, LpInteger)
            model += x == value
            variables.append(x)

        maxi = Formulations.maximum(model, variables, 1, 9)
        model.writeLP(str(self.get_lp_filename()))
        model.solve(self.get_application('maximum'))
        self.assertEqual(expected, maxi.varValue)

    def test_maximum(self) -> None:
        self.maximum([1, 2, 3], 3)
        self.maximum([3, 2, 1], 3)
        self.maximum([2, 2, 2], 2)

    def logical_not(self, value: int, expected: int) -> None:
        model = LpProblem("logical_not", LpMinimize)
        x = LpVariable("x", 0, 1, LpInteger)
        model += x == value
        y = Formulations.logical_not(model, x)
        model.writeLP(str(self.get_lp_filename()))
        model.solve(self.get_application('logical_not'))
        self.assertEqual(expected, y.varValue)

    def test_logical_not(self):
        self.logical_not(1, 0)
        self.logical_not(0, 1)

    def logical_or(self, value1: int, value2: int, expected: int) -> None:
        model = LpProblem("logical_or", LpMinimize)
        x1 = LpVariable("x1", 0, 1, LpInteger)
        x2 = LpVariable("x2", 0, 1, LpInteger)
        model += x1 == value1
        model += x2 == value2
        y = Formulations.logical_or(model, [x1, x2])
        model.writeLP(str(self.get_lp_filename()))
        model.solve(self.get_application('logical_or'))
        self.assertEqual(expected, y.varValue)

    def test_logical_or(self):
        self.logical_or(0, 0, 0)
        self.logical_or(0, 1, 1)
        self.logical_or(1, 0, 1)
        self.logical_or(1, 1, 1)

    def logical_and(self, value1: int, value2: int, expected: int) -> None:

        model = LpProblem("logical_and", LpMinimize)
        x1 = LpVariable("x1", 0, 1, LpInteger)
        x2 = LpVariable("x2", 0, 1, LpInteger)
        model += x1 == value1
        model += x2 == value2
        y = Formulations.logical_and(model, [x1, x2])
        model.writeLP(str(self.get_lp_filename()))
        model.solve(self.get_application('logical_and'))
        self.assertEqual(expected, y.varValue)

    def test_logical_and(self):
        self.logical_and(0, 0, 0)
        self.logical_and(0, 1, 0)
        self.logical_and(1, 0, 0)
        self.logical_and(1, 1, 1)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
