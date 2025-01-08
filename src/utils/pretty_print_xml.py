"""PrettyPrintXML function."""

from xml.dom.minidom import Document, Element, parseString

from defusedxml.ElementTree import fromstring, tostring


def pretty_print_xml(xml_string: str) -> str:
    """Convert a string into XML and pretty-prints it without the XML declaration.

    Args:
        xml_string (str): The input string representing XML.

    Returns:
        str: The pretty-printed XML string.
    """
    try:
        root: Element = fromstring(xml_string, forbid_dtd=True, forbid_entities=True)
    except Exception as error:
        return f'Error parsing XML: {error}'

    raw_xml: str = tostring(root, encoding='unicode')  # Convert to string
    parsed: Document = parseString(raw_xml)
    pretty_xml: str = parsed.toprettyxml(indent='  ', newl='\n')

    # Remove the XML declaration
    return '\n'.join(
        line for line in pretty_xml.splitlines() if line.strip() and not line.startswith('<?xml')
    )
