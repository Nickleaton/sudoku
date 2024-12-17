"""PrettyXML."""
from typing import Optional
from xml.dom.minidom import Document

from defusedxml.minidom import parseString  # Secure XML parsing


class PrettyXML:
    """Handles XML strings, their DOM representation, and formatted output."""

    def __init__(self, indent: str = '  '):
        """
        Initialize the PrettyXML class.

        Args:
            indent (str): Indentation used for pretty-printing XML.
        """
        self._indent: str = indent
        self._raw_string: str = ''
        self._dom: Optional[Document] = None
        self._pretty_string: str = ''

    def update_from_raw(self) -> None:
        """Parse raw XML string and update the DOM and pretty-printed string."""
        self._dom = parseString(self._raw_string)
        self._pretty_string = self._dom.toprettyxml(indent=self._indent)

    def update_from_dom(self) -> None:
        """
        Update the raw XML string and the pretty-printed XML string from the DOM.

        Raises:
            ValueError: If the DOM is not initialized.
        """
        if not self._dom:
            raise ValueError('DOM is not initialized')
        self._raw_string = self._dom.toxml()
        self._pretty_string = self._dom.toprettyxml(indent=self._indent)

    @property
    def raw_string(self) -> str:
        """
        Get the raw XML string.

        Returns:
            str: The unformatted XML string.
        """
        return self._raw_string

    @raw_string.setter
    def raw_string(self, xml_input: str) -> None:
        """
        Set a new raw XML string and update the DOM.

        Args:
            xml_input (str): The raw XML string to set.

        Raises:
            ValueError: If the input XML string is invalid.
        """
        self._raw_string = xml_input
        try:
            self.update_from_raw()
        except Exception as error:
            raise ValueError(f'Invalid XML string: {error}') from error

    @property
    def dom(self) -> Document:
        """
        Get the DOM representation of the XML string.

        Returns:
            Document: The DOM object for the XML.

        Raises:
            ValueError: If the DOM is not initialized.
        """
        if not self._dom:
            raise ValueError('DOM is not initialized')
        return self._dom

    @dom.setter
    def dom(self, document: Document) -> None:
        """
        Set a new DOM and update the XML string.

        Args:
            document (Document): A new DOM object to set.

        Raises:
            ValueError: If the input is not a valid DOM object.
        """
        if not isinstance(document, Document):
            raise ValueError('Provided DOM must be an instance of xml.dom.minidom.Document')
        self._dom = document
        self.update_from_dom()

    @property
    def pretty_string(self) -> str:
        """
        Get the pretty-printed XML string.

        Returns:
            str: The formatted XML string.
        """
        return self._pretty_string

    def reload(self) -> None:
        """Reparse the raw XML string to refresh the DOM and pretty string."""
        self.update_from_raw()

    def __str__(self) -> str:
        """
        Convert the object to its pretty-printed XML string.

        Returns:
            str: The pretty-printed XML string.
        """
        return self.pretty_string
