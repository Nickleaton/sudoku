import os
import re
import unittest
from typing import Optional, Dict

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

    @staticmethod
    def get_solution(problem: Dict) -> Optional[Solution]:
        for item in problem:
            if isinstance(item, Solution):
                return item
        return None

    def test_solve(self) -> None:
        filename = os.path.join("problems", "problem001.yaml")
        with open(filename, 'r', encoding="utf-8") as file:
            config = yaml.load(file, yaml.SafeLoader)

        board = Board.create('Board', config)

        problem = Item.create(board, {'Constraints': config['Constraints']})
        solver = PulpSolver(board)

        problem.add_constraint(solver, None, re.compile("Solution"))

        solver.solve()
        # print(str(solver.solution))

        expected = self.get_solution(problem)

        if expected is None:
            print("No solution specified")
            return
        self.assertEqual(expected, solver.answer)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
