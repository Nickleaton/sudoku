from src.items.line import Line


class Thermometer(Line):

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Thermometer', 'Comparison'})

    def css(self) -> str:
        return (
            ".Thermometer {\n"
            "    stroke: grey;\n"
            "    stroke-width: 20;\n"
            "    stroke-linecap: round;\n"
            "    stroke-linejoin: round;\n"
            "    fill-opacity: 0\n"
            "}\n"
        )

    def css2(self):
        return {
            ".Thermometer": {
                "stroke": "grey",
                "stroke-width": 20,
                "stroke-linecap": "round",
                "stroke-linejoin": "round",
                "fill-opacity": 0
            }
        }
