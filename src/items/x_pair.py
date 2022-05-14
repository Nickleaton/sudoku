from src.items.sum_pair import SumPair
from src.solvers.pulp_solver import PulpSolver


class XPair(SumPair):

    @property
    def total(self) -> int:
        return 10

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'X'})

    @property
    def label(self) -> str:
        return "X"

    def add_constraint(self, solver: PulpSolver) -> None:
        super().add_constraint(solver)
        self.add_unique_constraint(solver, True)
        self.add_allowed_constraint(solver, self.cells, [1, 2, 3, 4, 6, 7, 8, 9])

    def css(self) -> str:
        return (
            ".XPairForeground {\n"
            "    font-size: 30px;\n"
            "    stroke: black;\n"
            "    stroke-width: 1;\n"
            "    fill: black\n"
            "}\n"
            "\n"
            ".XPairBackground {\n"
            "    font-size: 30px;\n"
            "    stroke: white;\n"
            "    stroke-width: 8;\n"
            "    fill: white;\n"
            "    font-weight: bolder\n"
            "}\n"
            "\n"
        )

    def css2(self):
        return {
            ".XPairForeground": {
                "font-size": "30px",
                "stroke": "black",
                "stroke-width": 1,
                "fill": "black"
            },
            ".XPairBackground": {
                "font-size": "30px",
                "stroke": "white",
                "stroke-width": 8,
                "fill": "white",
                "font-weight": "bolder"
            }
        }
