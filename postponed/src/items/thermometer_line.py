"""ThermometerLine."""

from postponed.src.items.line import Line


class ThermometerLine(Line):
    """Thermometer line.

    Digits increase along the line.
    """

    @property
    def tags(self) -> set[str]:
        """Tags associated with the Thermometer line.

        Returns:
            set[str]: A set of tags specific to the Thermometer line, combined with inherited tags.
        """
        return super().tags.union({self.__class__.__name__, 'Comparison'})

    def css(self) -> dict:
        """CSS styling properties for rendering the Thermometer line.

        Returns:
            dict: A dictionary defining CSS properties for the Thermometer line.
        """
        return {
            '.ThermometerLine': {
                'stroke': 'grey',
                'stroke-width': 25,
                'stroke-linecap': 'round',
                'stroke-linejoin': 'round',
                'fill-opacity': 0,
            },
        }
