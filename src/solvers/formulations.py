from typing import List

from pulp import LpVariable, LpElement, LpInteger, lpSum

from src.solvers.pulp_solver import PulpSolver


class Formulations:

    @staticmethod
    def disjunction(solver: PulpSolver, var: LpElement, l1: int, u1: int, l2: int, u2: int) -> None:
        isupper = LpVariable(f"Disjunction_{var.name}_isupper", lowBound=0, upBound=1, cat=LpInteger)
        solver.model += var <= u1 + (u2 - u1) * isupper, f"Disjunction_{var.name}_a"
        solver.model += var <= l1 + (l2 - l1) * isupper, f"Disjunction_{var.name}_b"

    @staticmethod
    def product_binary_binary(solver: PulpSolver, d1: LpElement, d2: LpElement, d3: LpVariable) -> None:
        solver.model += d3 <= d1, f"Binary_Binary_{d3.name}_a"
        solver.model += d3 <= d2, f"Binary_Binary_{d3.name}_b"
        solver.model += d3 >= d1 + d2 - 1, f"Binary_Binary_{d3.name}_c"

    @staticmethod
    def product_binary_var(solver: PulpSolver, var: LpElement, x: LpElement, target: LpVariable, l: int, u: int) -> None:
        solver.model += l * var <= target, f"Product_Binary_{target.name}_a"
        solver.model += target <= u * var, f"Product_Binary_{target.name}_b"
        solver.model += l * (1 - var) <= x - target, f"Product_Binary_{target.name}_c"
        solver.model += x - target <= u * (1 - var), f"Product_Binary_{target.name}_d"

    @staticmethod
    def logical_and(solver: PulpSolver, target: LpVariable, variables: List[LpVariable]):
        n = len(variables)
        for var in variables:
            solver.model += target <= var, f"Logical_And_{target.name}_{var.name}_a"
        solver.model += target >= lpSum(variables) - (n - 1), f"Logical_And_{target.name}_b"

    @staticmethod
    def logical_or(solver: PulpSolver, target: LpVariable, variables: List[LpVariable]):
        pass  # TODO

