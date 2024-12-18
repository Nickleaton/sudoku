from defusedxml.ElementTree import fromstring, tostring
from defusedxml.minidom import parseString


def pretty_print_xml(xml_string: str) -> str:
    '''
    Converts a string into XML and pretty-prints it without the XML declaration.

    Args:
        xml_string (str): The input string representing XML.

    Returns:
        str: The pretty-printed XML string.
    '''
    try:
        root = fromstring(xml_string)  # Secure XML parsing
    except Exception as error:
        return f'Error parsing XML: {error}'

    raw_xml = tostring(root, encoding='unicode')  # Convert to string
    parsed = parseString(raw_xml)  # Pretty-print securely
    pretty_xml = parsed.toprettyxml(indent='  ', newl='\n')

    # Remove the XML declaration
    return '\n'.join(
        line for line in pretty_xml.splitlines() if line.strip() and not line.startswith('<?xml')
    )
