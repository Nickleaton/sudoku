# import unittest
#
# from pulp import LpVariable, LpInteger, LpProblem, LpMinimize
#
# from src.solvers.formulations import Formulations
#
#
# class TestFormulation(unittest.TestCase):
#
#     def setUp(self) -> None:
#         self.objective = 0, "Objective"
#         self.model = LpProblem("Sudoku", LpMinimize)
#
#     def test_mimimum(self):
#         count = 3
#         minimum = LpVariable("minimum", 1, 9, LpInteger)
#         maximum = LpVariable("maximum", 1, 9, LpInteger)
#         indicators_min = LpVariable.dicts("Indicators_min", (list(range(0, count))), 0, 1, LpInteger)
#         indicators_max = LpVariable.dicts("Indicators_max", (list(range(0, count))), 0, 1, LpInteger)
#         variables = LpVariable.dicts("Variables", (list(range(0, count))), 0, 1, LpInteger)
#
#         self.model += variables[0] == 7
#         self.model += variables[1] == 3
#         self.model += variables[2] == 5
#
#         Formulations.minimum(self.model, 0, 10, minimum, variables, indicators_min)
#         Formulations.maximum(self.model, 0, 10, maximum, variables, indicators_max)
#
#         self.model.writeLP(r"formulations.lp")
#         self.model.solve()
#         print (minimum.varValue)
#         print (maximum.varValue)
#
#
# if __name__ == '__main__':  # pragma: no cover
#     unittest.main()
