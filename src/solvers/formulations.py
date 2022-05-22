from typing import List

from pulp import LpVariable, LpElement, LpInteger, lpSum

from src.solvers.pulp_solver import PulpSolver


class Formulations:
    count = 0

    @staticmethod
    def parity(solver: PulpSolver, row: int, column: int) -> lpSum:
        return lpSum(
            [
                solver.choices[2][row][column],
                solver.choices[4][row][column],
                solver.choices[6][row][column],
                solver.choices[8][row][column]
            ]
        )

    # pylint: disable=too-many-arguments
    @staticmethod
    def disjunction(
            solver: PulpSolver,
            var: LpElement,
            lower_1: int,
            upper_1: int,
            lower_2: int,
            upper_2: int
    ) -> None:
        isupper = LpVariable(f"Disjunction_{var.name}_isupper", lowBound=0, upBound=1, cat=LpInteger)
        solver.model += var <= upper_1 + (upper_2 - upper_1) * isupper, f"Disjunction_{var.name}_a"
        solver.model += var <= lower_1 + (lower_2 - lower_1) * isupper, f"Disjunction_{var.name}_b"

    @staticmethod
    def product_binary_binary(
            solver: PulpSolver,
            decision_1: LpElement,
            decision_2: LpElement,
            decision_3: LpVariable
    ) -> None:
        solver.model += decision_3 <= decision_1, f"Binary_Binary_{decision_3.name}_a"
        solver.model += decision_3 <= decision_2, f"Binary_Binary_{decision_3.name}_b"
        solver.model += decision_3 >= decision_1 + decision_2 - 1, f"Binary_Binary_{decision_3.name}_c"

    # pylint: disable=too-many-arguments
    @staticmethod
    def product_binary_var(
            solver: PulpSolver,
            variable: LpElement,
            x: LpElement,
            target: LpVariable,
            lower: int,
            upper: int
    ) -> None:
        solver.model += lower * variable <= target, f"Product_Binary_{target.name}_a"
        solver.model += target <= upper * variable, f"Product_Binary_{target.name}_b"
        solver.model += lower * (1 - variable) <= x - target, f"Product_Binary_{target.name}_c"
        solver.model += x - target <= upper * (1 - variable), f"Product_Binary_{target.name}_d"

    @staticmethod
    def logical_and(solver: PulpSolver, target: LpVariable, variables: List[LpVariable]) -> None:
        n = len(variables)
        for var in variables:
            solver.model += target <= var, f"Logical_And_{target.name}_{var.name}_a"
        solver.model += target >= lpSum(variables) - (n - 1), f"Logical_And_{target.name}_b"

    @staticmethod
    def logical_or(solver: PulpSolver, target: LpVariable, variables: List[LpVariable]) -> None:
        pass

    @staticmethod
    def abs(solver: PulpSolver, x1: LpVariable, x2: LpVariable, upper: int) -> LpElement:
        d = LpVariable(f"Abs_Indicator_{Formulations.count}", 0, 1, LpInteger)
        difference = LpVariable(f"Abs_Difference_{Formulations.count}", 0, upper, LpInteger)
        solver.model += 0 <= difference - (x1 - x2), f"Abs_{Formulations.count}_a"
        solver.model += difference - (x1 - x2) <= 2 * upper * (1 - d), f"Abs_{Formulations.count}_b"
        solver.model += 0 <= difference - (x2 - x1), f"Abs_{Formulations.count}_c"
        solver.model += difference - (x2 - x1) <= 2 * upper * d, f"Abs_{Formulations.count}_d"
        Formulations.count += 1
        return difference
