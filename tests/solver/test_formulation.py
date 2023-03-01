import os
import unittest
from typing import List

from pulp import LpVariable, LpInteger, LpProblem, LpMinimize, getSolver, LpSolver, LpContinuous

from src.solvers.formulations import Formulations


class TestFormulation(unittest.TestCase):

    def setUp(self) -> None:
        log_path = os.path.join("output", "formulations", "logs")
        if not os.path.exists(log_path):  # pragma: no cover
            os.makedirs(log_path)
        lp_path = os.path.join("output", "formulations", "lp")
        if not os.path.exists(lp_path):  # pragma: no cover
            os.makedirs(lp_path)

    @staticmethod
    def get_application(name: str) -> LpSolver:
        log_path = os.path.join("output", "formulations", "logs")
        return getSolver('PULP_CBC_CMD', logPath=os.path.join(log_path, name + ".log"), msg=False, timeLimit=60)

    def absolute_int(self, v1: int, v2: int, expected: int) -> None:
        model = LpProblem("Sudoku", LpMinimize)
        absolute = LpVariable("minimum", 0, 9, LpInteger)
        x1 = LpVariable("x1", 1, 9, LpInteger)
        x2 = LpVariable("x2", 1, 9, LpInteger)

        model += x1 == v1
        model += x2 == v2
        model += absolute == Formulations.abs(model, x1, x2, 9)
        model.writeLP(os.path.join("output", "formulations", "lp", "absolute.lp"))
        model.solve(TestFormulation.get_application('absolute'))
        self.assertEqual(expected, absolute.varValue)

    def test_absolute_int(self) -> None:
        self.absolute_int(3, 9, 6)
        self.absolute_int(5, 3, 2)
        self.absolute_int(1, 1, 0)

    def absolute_float(self, v1: float, v2: float, expected: float) -> None:
        model = LpProblem("Sudoku", LpMinimize)
        absolute = LpVariable("minimum", 0, 9, LpContinuous)
        x1 = LpVariable("x1", 1, 9, LpContinuous)
        x2 = LpVariable("x2", 1, 9, LpContinuous)

        model += x1 == v1
        model += x2 == v2
        model += absolute == Formulations.abs(model, x1, x2, 9)
        model.writeLP(os.path.join("output", "formulations", "lp", "absolute.lp"))
        model.solve(TestFormulation.get_application('absolute'))
        self.assertEqual(expected, absolute.varValue)

    def test_absolute_float(self) -> None:
        self.absolute_float(3.0, 9.0, 6.0)
        self.absolute_float(5.0, 3.0, 2.0)
        self.absolute_float(1.0, 1.0, 0.0)
        self.absolute_float(1.5, 2.8, 1.3)
        self.absolute_float(4.5, 2.8, 1.7)

    def minimum(self, values: List[int], expected: int) -> None:
        model = LpProblem("Sudoku", LpMinimize)
        variables: List[LpVariable] = []
        for i, value in enumerate(values):
            x = LpVariable(f"x{i}", 1, 9, LpInteger)
            model += x == value
            variables.append(x)

        mini = Formulations.minimum(model, variables, 1, 9)
        model.writeLP(os.path.join("output", "formulations", "lp", "minimum.lp"))
        model.solve(TestFormulation.get_application('minimum'))
        self.assertEqual(expected, mini.varValue)

    def test_minimum(self) -> None:
        self.minimum([2, 2, 2], 2)
        self.minimum([1, 2, 3], 1)
        self.minimum([3, 2, 1], 1)

    def maximum(self, values: List[int], expected: int) -> None:
        model = LpProblem("Sudoku", LpMinimize)
        variables: List[LpVariable] = []
        for i, value in enumerate(values):
            x = LpVariable(f"x{i}", 1, 9, LpInteger)
            model += x == value
            variables.append(x)

        maxi = Formulations.maximum(model, variables, 1, 9)
        model.writeLP(os.path.join("output", "formulations", "lp", "maximum.lp"))
        model.solve(TestFormulation.get_application('maximum'))
        self.assertEqual(expected, maxi.varValue)

    def test_maximum(self) -> None:
        self.maximum([1, 2, 3], 3)
        self.maximum([3, 2, 1], 3)
        self.maximum([2, 2, 2], 2)

    def logical_not(self, value: int, expected: int) -> None:
        model = LpProblem("Sudoku", LpMinimize)
        x = LpVariable("x", 0, 1, LpInteger)
        model += x == value
        y = Formulations.logical_not(model, x)
        model.writeLP(os.path.join("output", "formulations", "lp", "logical_not.lp"))
        model.solve(TestFormulation.get_application('logical_not'))
        self.assertEqual(expected, y.varValue)

    def test_logical_not(self):
        self.logical_not(1, 0)
        self.logical_not(0, 1)

    def logical_or(self, value1: int, value2: int, expected: int) -> None:
        model = LpProblem("Sudoku", LpMinimize)
        x1 = LpVariable("x1", 0, 1, LpInteger)
        x2 = LpVariable("x2", 0, 1, LpInteger)
        model += x1 == value1
        model += x2 == value2
        y = Formulations.logical_or(model, [x1, x2])
        model.writeLP(os.path.join("output", "formulations", "lp", "logical_or.lp"))
        model.solve(TestFormulation.get_application('logical_or'))
        self.assertEqual(expected, y.varValue)

    def test_logical_or(self):
        self.logical_or(0, 0, 0)
        self.logical_or(0, 1, 1)
        self.logical_or(1, 0, 1)
        self.logical_or(1, 1, 1)

    def logical_and(self, value1: int, value2: int, expected: int) -> None:
        model = LpProblem("Sudoku", LpMinimize)
        x1 = LpVariable("x1", 0, 1, LpInteger)
        x2 = LpVariable("x2", 0, 1, LpInteger)
        model += x1 == value1
        model += x2 == value2
        y = Formulations.logical_and(model, [x1, x2])
        model.writeLP(os.path.join("output", "formulations", "lp", "logical_and.lp"))
        model.solve(TestFormulation.get_application('logical_and'))
        self.assertEqual(expected, y.varValue)

    def test_logical_and(self):
        self.logical_and(0, 0, 0)
        self.logical_and(0, 1, 0)
        self.logical_and(1, 0, 0)
        self.logical_and(1, 1, 1)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
