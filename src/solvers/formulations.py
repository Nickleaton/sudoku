from typing import List

from pulp import LpVariable, LpElement, LpInteger, lpSum, LpProblem, LpContinuous


class Formulations:
    count = 0

    # pylint: disable=too-many-arguments
    @staticmethod
    def disjunction(
            model: LpProblem,
            var: LpElement,
            lower_1: int,
            upper_1: int,
            lower_2: int,
            upper_2: int
    ) -> None:
        isupper = LpVariable(f"Disjunction_{var.name}_isupper", lowBound=0, upBound=1, cat=LpInteger)
        model += var <= upper_1 + (upper_2 - upper_1) * isupper, f"Disjunction_{var.name}_a"
        model += var <= lower_1 + (lower_2 - lower_1) * isupper, f"Disjunction_{var.name}_b"

    @staticmethod
    def product_binary_binary(
            model: LpProblem,
            decision_1: LpElement,
            decision_2: LpElement,
            decision_3: LpVariable
    ) -> None:
        model += decision_3 <= decision_1, f"Binary_Binary_{decision_3.name}_a"
        model += decision_3 <= decision_2, f"Binary_Binary_{decision_3.name}_b"
        model += decision_3 >= decision_1 + decision_2 - 1, f"Binary_Binary_{decision_3.name}_c"

    # pylint: disable=too-many-arguments
    @staticmethod
    def product_binary_var(
            model: LpProblem,
            variable: LpElement,
            x: LpElement,
            target: LpVariable,
            lower: int,
            upper: int
    ) -> None:
        model += lower * variable <= target, f"Product_Binary_{target.name}_a"
        model += target <= upper * variable, f"Product_Binary_{target.name}_b"
        model += lower * (1 - variable) <= x - target, f"Product_Binary_{target.name}_c"
        model += x - target <= upper * (1 - variable), f"Product_Binary_{target.name}_d"

    @staticmethod
    def logical_and(model: LpProblem, dis: List[LpVariable]) -> LpVariable:
        d = LpVariable(f"l_and_{Formulations.count}", 0, 1, LpInteger)
        n = len(dis)
        for di in dis:
            model += d <= di, f"Logical_And_{d.name}_{di.name}_a"
        model += d >= lpSum(dis) - (n - 1), f"Logical_And_{d.name}_b"
        return d

    @staticmethod
    def logical_or(model: LpProblem, dis: List[LpVariable]) -> LpVariable:
        d = LpVariable(f"l_and_{Formulations.count}", 0, 1, LpInteger)
        for di in dis:
            model += d >= di, f"Logical_or_{d.name}_{di.name}_a"
        model += d <= 1, f"Logical_or_{d.name}_b"
        return d

    @staticmethod
    def logical_not(model: LpProblem, di: LpVariable) -> LpVariable:
        d = LpVariable(f"l_not_{Formulations.count}", 0, 1, LpInteger)
        model += d == 1 - di, f"Logical_not_{di.name}"
        return d

    @staticmethod
    def abs(model: LpProblem, x1: LpVariable, x2: LpVariable, upper: int) -> LpVariable:
        d = LpVariable(f"Abs_Indicator_{Formulations.count}", 0, 1, LpInteger)
        y = LpVariable(f"Abs_Difference_{Formulations.count}", 0, upper, LpContinuous)
        model += 0 <= y - (x1 - x2), f"Abs_{Formulations.count}_a"
        model += y - (x1 - x2) <= 2 * upper * (1 - d), f"Abs_{Formulations.count}_b"
        model += 0 <= y - (x2 - x1), f"Abs_{Formulations.count}_c"
        model += y - (x2 - x1) <= 2 * upper * d, f"Abs_{Formulations.count}_d"
        Formulations.count += 1
        return y

    @staticmethod
    def minimum(model: LpProblem, xi: List[LpVariable], lower: int, upper: int) -> LpVariable:
        y = LpVariable(f"Minimum_{Formulations.count}", lower, upper, LpInteger)
        d = LpVariable.dicts(
            f"Minimum_{Formulations.count}_indicator",
            (range(0, len(xi))),
            0,
            1,
            LpInteger
        )
        for i, x in enumerate(xi):
            model += y <= x, f"Minimum_{Formulations.count}_{i}_a"
            model += y >= x - (upper - lower) * (1 - d[i]), f"Minimum_{Formulations.count}_{i}_b"
        model += lpSum(d) == 1, f"Minimum_{Formulations.count}_SOS"
        Formulations.count += 1
        return y

    @staticmethod
    def maximum(model: LpProblem, xi: List[LpVariable], lower: int, upper: int) -> LpVariable:
        y = LpVariable(f"Maximum_{Formulations.count}", lower, upper, LpInteger)
        d = LpVariable.dicts(
            f"Maximum_{Formulations.count}_indicator",
            (range(0, len(xi))),
            0,
            1,
            LpInteger
        )
        for i, x in enumerate(xi):
            model += y >= x, f"Maximum_{Formulations.count}_{i}_a"
            model += y <= x + (upper - lower) * (1 - d[i]), f"Maximum_{Formulations.count}_{i}_b"
        model += lpSum(d) == 1, f"Maximum_{Formulations.count}_SOS"
        Formulations.count += 1
        return y
