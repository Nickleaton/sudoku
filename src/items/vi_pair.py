from src.items.sum_pair import SumPair


class VIPair(SumPair):

    @property
    def total(self) -> int:
        return 6

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'VI'})

    @property
    def label(self) -> str:
        return "VI"

    def css(self) -> str:
        return (
            ".VIPairForeground {\n"
            "    font-size: 30px;\n"
            "    stroke: black;\n"
            "    stroke-width: 1;\n"
            "    fill: black\n"
            "}\n"
            "\n"
            ".VIPairBackground {\n"
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
            ".VIPairForeground": {
                "font-size": "30px",
                "stroke": "black",
                "stroke-width": 1,
                "fill": "black"
            },
            ".VIPairBackground": {
                "font-size": "30px",
                "stroke": "white",
                "stroke-width": 8,
                "fill": "white",
                "font-weight": "bolder"
            }
        }
