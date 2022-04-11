import os
import unittest

import oyaml as yaml

from src.items.board import Board
from src.items.item import Item
from src.items.solution import Solution
from src.solvers.pulp_solver import PulpSolver


class TestSolver(unittest.TestCase):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3)

    def test_setup(self):
        self.assertIsNotNone(self.board)

    def test_solve(self) -> None:
        fname = os.path.join("problems", "problem001.yaml")
        with open(fname, 'r') as f:
            config = yaml.load(f, yaml.SafeLoader)

        board = Board.create('Board', config)

        problem = Item.create('Constraints', board, config['Constraints'])
        solver = PulpSolver(board)

        problem.add_variables(board, solver)
        problem.add_constraint(solver)

        solver.solve()
        print(str(solver.solution))

        expected = Solution.create(problem.board, config['Solution'])

        self.assertEqual(expected, solver.solution)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
