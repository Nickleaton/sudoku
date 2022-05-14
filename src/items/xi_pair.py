from src.items.sum_pair import SumPair


class XIPair(SumPair):

    @property
    def total(self) -> int:
        return 11

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'XI'})

    @property
    def label(self) -> str:
        return "XI"

    def css(self) -> str:
        return (
            ".XIPairForeground {\n"
            "    font-size: 30px;\n"
            "    stroke: black;\n"
            "    stroke-width: 1;\n"
            "    fill: black\n"
            "}\n"
            "\n"
            ".XIPairBackground {\n"
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
            ".XIPairForeground": {
                "font-size": "30px",
                "stroke": "black",
                "stroke-width": 1,
                "fill": "black"
            },
            ".XIPairBackground": {
                "font-size": "30px",
                "stroke": "white",
                "stroke-width": 8,
                "fill": "white",
                "font-weight": "bolder"
            }
        }
