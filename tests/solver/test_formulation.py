import os
import unittest
from typing import List

from pulp import LpVariable, LpInteger, LpProblem, LpMinimize, getSolver, LpSolver

from src.solvers.formulations import Formulations


class TestFormulation(unittest.TestCase):

    def setUp(self) -> None:
        log_path = os.path.join("output", "formulations", "logs")
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        lp_path = os.path.join("output", "formulations", "lp")
        if not os.path.exists(lp_path):
            os.makedirs(lp_path)

    @staticmethod
    def get_application(name: str) -> LpSolver:
        log_path = os.path.join("output", "formulations", "logs")
        return getSolver('PULP_CBC_CMD', logPath=os.path.join(log_path, name + ".log"), msg=False, timeLimit=60)

    def absolute(self, v1: int, v2: int, expected: int):
        model = LpProblem("Sudoku", LpMinimize)
        absolute = LpVariable("minimum", 0, 9, LpInteger)
        x1 = LpVariable("x1", 1, 9, LpInteger)
        x2 = LpVariable("x2", 1, 9, LpInteger)

        model += x1 == v1
        model += x2 == v2
        model += absolute == Formulations.abs(model, x1, x2, 9)
        model.writeLP(os.path.join("output", "formulations", "lp", "absolute.lp"))
        model.solve(TestFormulation.get_application('absolute'))
        # print()
        # print(f"X1       {x1.varValue}")
        # print(f"X2       {x2.varValue}")
        # print(f"Absolute {absolute.varValue}")
        self.assertEqual(expected, absolute.varValue)

    def test_absolute(self):
        self.absolute(3, 9, 6)
        self.absolute(5, 3, 2)
        self.absolute(1, 1, 0)

    def minimum(self, values: List[int], expected: int):
        model = LpProblem("Sudoku", LpMinimize)
        variables: List[LpVariable] = []
        for i, value in enumerate(values):
            x = LpVariable(f"x{i}", 1, 9, LpInteger)
            model += x == value
            variables.append(x)

        mini = Formulations.minimum(model, variables, 1, 9)
        model.writeLP(os.path.join("output", "formulations", "lp", "minimum.lp"))
        model.solve(TestFormulation.get_application('minimum'))
        # print()
        # print(f"Values   {repr(values)}")
        # print(f"Minimum  {mini.varValue}")
        self.assertEqual(expected, mini.varValue)

    def test_minimum(self):
        self.minimum([2, 2, 2], 2)
        self.minimum([1, 2, 3], 1)
        self.minimum([3, 2, 1], 1)

    def maximum(self, values: List[int], expected: int):
        model = LpProblem("Sudoku", LpMinimize)
        variables: List[LpVariable] = []
        for i, value in enumerate(values):
            x = LpVariable(f"x{i}", 1, 9, LpInteger)
            model += x == value
            variables.append(x)

        maxi = Formulations.maximum(model, variables, 1, 9)
        model.writeLP(os.path.join("output", "formulations", "lp", "maximum.lp"))
        model.solve(TestFormulation.get_application('maximum'))
        # print()
        # print(f"Values   {repr(values)}")
        # print(f"Maximum  {maxi.varValue}")
        self.assertEqual(expected, maxi.varValue)

    def test_maximum(self):
        self.maximum([1, 2, 3], 3)
        self.maximum([3, 2, 1], 3)
        self.maximum([2, 2, 2], 2)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
