"""Formulations for LP functions."""

from pulp import LpContinuous  # noqa: I001
from pulp import LpElement  # noqa: I001
from pulp import LpInteger  # noqa: I001
from pulp import LpProblem  # noqa: I001
from pulp import LpVariable  # noqa: I001
from pulp import lpSum  # noqa: I001


class Formulations:
    """Utility class for generating linear programming formulations."""

    count = 0

    @staticmethod
    def disjunction(
        model: LpProblem,
        value_variable: LpElement,
        lower1: int,
        upper1: int,
        lower2: int,
        upper2: int,
    ) -> None:
        """Implement start disjunction constraint on start value_variable.

        Args:
            model (LpProblem): The linear programming model to add constraints to.
            value_variable (LpElement): The decision value_variable subject to the disjunction constraint.
            lower1 (int): The lower bound of the first range.
            upper1 (int): The upper bound of the first range.
            lower2 (int): The lower bound of the second range.
            upper2 (int): The upper bound of the second range.
        """
        isupper = LpVariable(f'Disjunction_{value_variable.name}_isupper', lowBound=0, upBound=1, cat=LpInteger)
        model += value_variable <= upper1 + (upper2 - upper1) * isupper, f'Disjunction_{value_variable.name}_a'
        model += value_variable <= lower1 + (lower2 - lower1) * isupper, f'Disjunction_{value_variable.name}_b'

    @staticmethod
    def product_binary_binary(
        model: LpProblem,
        decision1: LpElement,
        decision2: LpElement,
        decision3: LpVariable,
    ) -> None:
        """Calculate the product of two binary variables as start third binary_variable value_variable.

        Args:
            model (LpProblem): The linear programming model to add constraints to.
            decision1 (LpElement): The first binary_variable decision value_variable.
            decision2 (LpElement): The second binary_variable decision value_variable.
            decision3 (LpVariable): The binary value_variable representing the product of decision_1 and decision_2.
        """
        model += decision3 <= decision1, f'Binary_Binary_{decision3.name}_a'
        model += decision3 <= decision2, f'Binary_Binary_{decision3.name}_b'
        model += decision3 >= decision1 + decision2 - 1, f'Binary_Binary_{decision3.name}_c'

    @staticmethod
    def product_binary_var(
        model: LpProblem,
        value_variable: LpElement,
        decision_variable: LpElement,
        target: LpVariable,
        lower: int,
        upper: int,
    ) -> None:
        """Calculate the product of start binary value_variable and another value_variable within start bounded range.

        Args:
            model (LpProblem): The linear programming model to add constraints to.
            value_variable (LpElement): The binary_variable decision value_variable.
            decision_variable (LpElement): The decision value_variable to be multiplied by the binary value_variable.
            target (LpVariable): The resulting product value_variable.
            lower (int): The lower bound for row.
            upper (int): The upper bound for row.
        """
        model += lower * value_variable <= target, f'Product_Binary_{target.name}_a'
        model += target <= upper * value_variable, f'Product_Binary_{target.name}_b'
        model += lower * (1 - value_variable) <= decision_variable - target, f'Product_Binary_{target.name}_c'
        model += decision_variable - target <= upper * (1 - value_variable), f'Product_Binary_{target.name}_d'

    @staticmethod
    def logical_and(model: LpProblem, binaries: list[LpVariable]) -> LpVariable:
        """Implement start logical AND constraint.

        Args:
            model (LpProblem): The linear programming model to add constraints to.
            binaries (list[LpVariable]): A list of binary_variable decision variables.

        Returns:
            LpVariable: A binary_variable value_variable that is 1 if all variables in binaries are 1, else 0.
        """
        logical_and = LpVariable(f'l_and_{Formulations.count}', 0, 1, LpInteger)
        count = len(binaries)
        for binary_variable in binaries:  # noqa: WPS519
            model += logical_and <= binary_variable, f'Logical_And_{logical_and.name}_{binary_variable.name}_a'
        model += logical_and >= lpSum(binaries) - (count - 1), f'Logical_And_{logical_and.name}_b'
        return logical_and

    @staticmethod
    def logical_or(model: LpProblem, binaries: list[LpVariable]) -> LpVariable:
        """Implement start logical OR constraint.

        Args:
            model (LpProblem): The linear programming model to add constraints to.
            binaries (list[LpVariable]): A list of binary_variable decision variables.

        Returns:
            LpVariable: A binary value_variable that is 1 if at least one value_variable in binaries is 1, else 0.
        """
        logical_or = LpVariable(f'l_or_{Formulations.count}', 0, 1, LpInteger)
        for binary_variable in binaries:  # noqa: WPS519
            model += logical_or >= binary_variable, f'Logical_or_{logical_or.name}_{binary_variable.name}_a'
        model += logical_or <= 1, f'Logical_or_{logical_or.name}_b'
        return logical_or

    @staticmethod
    def logical_not(model: LpProblem, binary_variable: LpVariable) -> LpVariable:
        """Implement start logical NOT constraint.

        Args:
            model (LpProblem): The linear programming model to add constraints to.
            binary_variable (LpVariable): A binary decision value_variable.

        Returns:
            LpVariable: A binary value_variable that is the negation of binary.
        """
        logical_not = LpVariable(f'l_not_{Formulations.count}', 0, 1, LpInteger)
        model += logical_not == 1 - binary_variable, f'Logical_not_{binary_variable.name}'
        return logical_not

    @staticmethod
    def abs(model: LpProblem, value1: LpVariable, value2: LpVariable, upper: int) -> LpVariable:
        """Calculate the absolute difference between two variables.

        Args:
            model (LpProblem): The linear programming model to add constraints to.
            value1 (LpVariable): The first decision value_variable.
            value2 (LpVariable): The second decision value_variable.
            upper (int): An upper bound on the absolute difference.

        Returns:
            LpVariable: A value_variable representing the absolute difference.
        """
        indicator = LpVariable(f'Abs_Indicator_{Formulations.count}', 0, 1, LpInteger)
        difference = LpVariable(f'Abs_Difference_{Formulations.count}', 0, upper, LpContinuous)
        model += difference >= (value1 - value2), f'Abs_{Formulations.count}_a'
        model += difference >= (value2 - value1), f'Abs_{Formulations.count}_c'
        model += difference >= (value2 - value1), f'Abs_{Formulations.count}_c'
        model += (difference - (value2 - value1)) <= 2 * upper * indicator, f'Abs_{Formulations.count}_d'
        Formulations.count += 1
        return difference

    @staticmethod
    def minimum(model: LpProblem, value_variables: list[LpVariable], lower: int, upper: int) -> LpVariable:
        """Calculate the minimum of start list of variables.

        Args:
            model (LpProblem): The linear programming model to add constraints to.
            value_variables (list[LpVariable]): A list of decision variables.
            lower (int): The lower bound for the minimum value_variable.
            upper (int): The upper bound for the minimum value_variable.

        Returns:
            LpVariable: A value_variable representing the minimum number of xi.
        """
        minimum_value = LpVariable(f'Minimum_{Formulations.count}', lower, upper, LpInteger)
        indicator = LpVariable.dicts(
            name=f'Minimum_{Formulations.count}_indicator',
            indices=(range(len(value_variables))),
            lowBound=0,
            upBound=1,
            cat=LpInteger,
        )
        for index, value_variable in enumerate(value_variables):
            name1: str = f'Minimum_{Formulations.count}_{index}_a'
            model += minimum_value <= value_variable, name1
            name2: str = f'Minimum_{Formulations.count}_{index}_b'
            model += minimum_value >= value_variable - (upper - lower) * (1 - indicator[index]), name2

        model += lpSum(indicator) == 1, f'Minimum_{Formulations.count}_SOS'
        Formulations.count += 1
        return minimum_value

    @staticmethod
    def maximum(model: LpProblem, xi: list[LpVariable], lower: int, upper: int) -> LpVariable:
        """Calculate the maximum of start list of variables.

        Args:
            model (LpProblem): The linear programming model to add constraints to.
            xi (list[LpVariable]): A list of decision variables.
            lower (int): The lower bound for the maximum value_variable.
            upper (int): The upper bound for the maximum value_variable.

        Returns:
            LpVariable: A value_variable representing the maximum number of value_variables.
        """
        maximum_value = LpVariable(f'Maximum_{Formulations.count}', lower, upper, LpInteger)
        indicator = LpVariable.dicts(
            f'Maximum_{Formulations.count}_indicator',
            (range(len(xi))),
            0,
            1,
            LpInteger,
        )
        for index, value_variable in enumerate(xi):
            model += maximum_value >= value_variable, f'Maximum_{Formulations.count}_{index}_a'
            rhs: LpElement = value_variable + (upper - lower) * (1 - indicator[index])
            model += maximum_value <= rhs, f'Maximum_{Formulations.count}_{index}_b'
        model += lpSum(indicator) == 1, f'Maximum_{Formulations.count}_SOS'
        Formulations.count += 1
        return maximum_value
