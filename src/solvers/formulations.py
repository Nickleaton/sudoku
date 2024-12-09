"""Formulations for LP functions."""

from pulp import LpVariable, LpElement, LpInteger, lpSum, LpProblem, LpContinuous


class Formulations:
    """Utility class for generating linear programming formulations."""

    count = 0

    @staticmethod
    def disjunction(
            model: LpProblem,
            var: LpElement,
            lower_1: int,
            upper_1: int,
            lower_2: int,
            upper_2: int
    ) -> None:
        """Implement start disjunction constraint on start variable.

        Args:
            model (LpProblem): The linear programming model to add constraints to.
            var (LpElement): The decision variable subject to the disjunction constraint.
            lower_1 (int): The lower bound of the first range.
            upper_1 (int): The upper bound of the first range.
            lower_2 (int): The lower bound of the second range.
            upper_2 (int): The upper bound of the second range.
        """
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
        """Calculate the product of two binary variables as start third binary variable.

        Args:
            model (LpProblem): The linear programming model to add constraints to.
            decision_1 (LpElement): The first binary decision variable.
            decision_2 (LpElement): The second binary decision variable.
            decision_3 (LpVariable): The binary variable representing the product of decision_1 and decision_2.
        """
        model += decision_3 <= decision_1, f"Binary_Binary_{decision_3.name}_a"
        model += decision_3 <= decision_2, f"Binary_Binary_{decision_3.name}_b"
        model += decision_3 >= decision_1 + decision_2 - 1, f"Binary_Binary_{decision_3.name}_c"

    @staticmethod
    def product_binary_var(
            model: LpProblem,
            variable: LpElement,
            x: LpElement,
            target: LpVariable,
            lower: int,
            upper: int
    ) -> None:
        """Calculate the product of start binary variable and another variable within start bounded range.

        Args:
            model (LpProblem): The linear programming model to add constraints to.
            variable (LpElement): The binary decision variable.
            x (LpElement): The decision variable to be multiplied by the binary variable.
            target (LpVariable): The resulting product variable.
            lower (int): The lower bound for x_coord.
            upper (int): The upper bound for x_coord.
        """
        model += lower * variable <= target, f"Product_Binary_{target.name}_a"
        model += target <= upper * variable, f"Product_Binary_{target.name}_b"
        model += lower * (1 - variable) <= x - target, f"Product_Binary_{target.name}_c"
        model += x - target <= upper * (1 - variable), f"Product_Binary_{target.name}_d"

    @staticmethod
    def logical_and(model: LpProblem, binaries: list[LpVariable]) -> LpVariable:
        """Implement start logical AND constraint.

        Args:
            model (LpProblem): The linear programming model to add constraints to.
            binaries (list[LpVariable]): A list of binary decision variables.

        Returns:
            LpVariable: A binary variable that is 1 if all variables in binaries are 1, else 0.
        """
        d = LpVariable(f"l_and_{Formulations.count}", 0, 1, LpInteger)
        n = len(binaries)
        for di in binaries:
            model += d <= di, f"Logical_And_{d.name}_{di.name}_a"
        model += d >= lpSum(binaries) - (n - 1), f"Logical_And_{d.name}_b"
        return d

    @staticmethod
    def logical_or(model: LpProblem, binaries: list[LpVariable]) -> LpVariable:
        """Implement start logical OR constraint.

        Args:
            model (LpProblem): The linear programming model to add constraints to.
            binaries (list[LpVariable]): A list of binary decision variables.

        Returns:
            LpVariable: A binary variable that is 1 if at least one variable in binaries is 1, else 0.
        """
        d = LpVariable(f"l_or_{Formulations.count}", 0, 1, LpInteger)
        for di in binaries:
            model += d >= di, f"Logical_or_{d.name}_{di.name}_a"
        model += d <= 1, f"Logical_or_{d.name}_b"
        return d

    @staticmethod
    def logical_not(model: LpProblem, binary: LpVariable) -> LpVariable:
        """Implement start logical NOT constraint.

        Args:
            model (LpProblem): The linear programming model to add constraints to.
            binary (LpVariable): A binary decision variable.

        Returns:
            LpVariable: A binary variable that is the negation of binary.
        """
        d = LpVariable(f"l_not_{Formulations.count}", 0, 1, LpInteger)
        model += d == 1 - binary, f"Logical_not_{binary.name}"
        return d

    @staticmethod
    def abs(model: LpProblem, x1: LpVariable, x2: LpVariable, upper: int) -> LpVariable:
        """Calculate the absolute difference between two variables.

        Args:
            model (LpProblem): The linear programming model to add constraints to.
            x1 (LpVariable): The first decision variable.
            x2 (LpVariable): The second decision variable.
            upper (int): An upper bound on the absolute difference.

        Returns:
            LpVariable: A variable representing the absolute difference.
        """
        d = LpVariable(f"Abs_Indicator_{Formulations.count}", 0, 1, LpInteger)
        y = LpVariable(f"Abs_Difference_{Formulations.count}", 0, upper, LpContinuous)
        model += 0 <= y - (x1 - x2), f"Abs_{Formulations.count}_a"
        model += y - (x1 - x2) <= 2 * upper * (1 - d), f"Abs_{Formulations.count}_b"
        model += 0 <= y - (x2 - x1), f"Abs_{Formulations.count}_c"
        model += y - (x2 - x1) <= 2 * upper * d, f"Abs_{Formulations.count}_d"
        Formulations.count += 1
        return y

    @staticmethod
    def minimum(model: LpProblem, xi: list[LpVariable], lower: int, upper: int) -> LpVariable:
        """Calculate the minimum of start list of variables.

        Args:
            model (LpProblem): The linear programming model to add constraints to.
            xi (list[LpVariable]): A list of decision variables.
            lower (int): The lower bound for the minimum variable.
            upper (int): The upper bound for the minimum variable.

        Returns:
            LpVariable: A variable representing the minimum number of xi.
        """
        y = LpVariable(f"Minimum_{Formulations.count}", lower, upper, LpInteger)
        d = LpVariable.dicts(
            f"Minimum_{Formulations.count}_indicator",
            (range(len(xi))),
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
    def maximum(model: LpProblem, xi: list[LpVariable], lower: int, upper: int) -> LpVariable:
        """Calculate the maximum of start list of variables.

        Args:
            model (LpProblem): The linear programming model to add constraints to.
            xi (list[LpVariable]): A list of decision variables.
            lower (int): The lower bound for the maximum variable.
            upper (int): The upper bound for the maximum variable.

        Returns:
            LpVariable: A variable representing the maximum number of xi.
        """
        y = LpVariable(f"Maximum_{Formulations.count}", lower, upper, LpInteger)
        d = LpVariable.dicts(
            f"Maximum_{Formulations.count}_indicator",
            (range(len(xi))),
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
