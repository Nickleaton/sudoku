from src.items.line import Line


class Thermometer(Line):

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Thermometer', 'Comparison'})
