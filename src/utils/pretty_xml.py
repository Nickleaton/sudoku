from xml.dom.minidom import parseString, Document


class PrettyXML:
    """
    A class to handle XML strings and provide their DOM and pretty-printed formats.
    """

    def __init__(self):
        """
        Initializes the PrettyXML class.

        Attributes:
            _raw_string (str): The original, unformatted XML string.
            _dom (xml.dom.minidom.Document | None): The DOM object representing the XML.
            _pretty_string (str): The formatted, pretty-printed XML string.
        """
        self._raw_string = ''
        self._dom = None
        self._pretty_string = ''

    def _update_from_raw(self) -> None:
        """
        Parses the raw XML string and updates the DOM and pretty-printed string.

        Raises:
            ValueError: If the raw XML string is invalid.
        """
        try:
            self._dom = parseString(self._raw_string)
            self._pretty_string = self._dom.toprettyxml(indent='  ')
        except Exception as e:
            raise ValueError(f'Invalid XML string: {e}')

    def _update_from_dom(self) -> None:
        """
        Updates the raw string and pretty-printed string from the DOM.

        Raises:
            ValueError: If the DOM object is not set.
        """
        if self._dom is None:
            raise ValueError('DOM is not set')
        self._raw_string = self._dom.toxml()
        self._pretty_string = self._dom.toprettyxml(indent='  ')

    @property
    def raw_string(self) -> str:
        """
        Gets the raw XML string.

        Returns:
            str: The original, unformatted XML string.
        """
        return self._raw_string

    @raw_string.setter
    def raw_string(self, value: str) -> None:
        """
        Sets the raw XML string and updates the DOM and pretty-printed string.

        Args:
            value (str): The new raw XML string.

        Raises:
            ValueError: If the input XML string is invalid.
        """
        self._raw_string = value
        self._update_from_raw()

    @property
    def dom(self) -> Document:
        """
        Gets the DOM representation of the XML string.

        Returns:
            xml.dom.minidom.Document: The DOM object representing the XML.

        Raises:
            ValueError: If the DOM is not initialized.
        """
        return self._dom

    @dom.setter
    def dom(self, value: Document) -> None:
        """
        Sets the DOM and updates the raw XML string and pretty-printed string.

        Args:
            value (xml.dom.minidom.Document): The new DOM object.

        Raises:
            ValueError: If the DOM is not set or invalid.
        """
        self._dom = value
        self._update_from_dom()

    @property
    def pretty_string(self) -> str:
        """
        Gets the pretty-printed version of the XML string.

        Returns:
            str: The formatted XML string with indentation.
        """
        return self._pretty_string
