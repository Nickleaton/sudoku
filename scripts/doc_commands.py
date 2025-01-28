"""Generate dot file for command documentation."""
import logging
import sys
from pathlib import Path

from graphviz import Source  # noqa: I005
from jinja2 import Template

from doc_commands_parser import create_arg_parser  # noqa: I001
from doc_commands_parser import validate_commands  # noqa: I001
from doc_commands_parser import validate_output_directory  # noqa: I001
from src.commands.command import Command  # noqa: I001
from src.utils.load_modules import load_modules  # noqa: I005


class DirectoryValidationError(Exception):
    """Raised when the output directory is invalid."""


class CommandValidationError(Exception):
    """Raised when no commands are found in Command.classes."""


# Define the Jinja2 template
template_string = """
digraph {
    rankdir=TB;
    node [shape=box];
    {% for cls_name, class_type in classes.items() %}
        {% for precondition in class_type().preconditions %}
            '{{ class_type().name }}' -> '{{ precondition().name }}';
        {% endfor %}
    {% endfor %}
}
"""


def setup_logging() -> None:
    """Set up logging for the script.

    Configures logging to output messages with a level of INFO or higher, formatted with
    timestamp, log level, and message.
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',  # noqa: WPS323
    )


def generate_dot_content() -> str:
    """Generate the DOT content using the Jinja2 template and Command.classes.

    Renders a DOT representation of the command dependencies, where each command is linked to its preconditions.

    Returns:
        str: The rendered DOT content as a string.
    """
    logging.info('Rendering DOT content...')
    template = Template(template_string)
    return template.render(classes=Command.classes)


def write_dot_file(dot_content: str, output_dir: Path) -> None:
    """Write the DOT content to a file.

    Args:
        dot_content (str): The DOT content to write to the file.
        output_dir (Path): The directory where the file will be saved.
    """
    dot_file_name: Path = output_dir / Path('commands.dot')
    logging.info(f'Writing DOT file to: {dot_file_name.name}')
    with dot_file_name.open('w') as dot_file:
        dot_file.write(dot_content)


def render_svg(dot_content: str, output_dir: Path) -> None:
    """Render the DOT content to an SVG file.

    Args:
        dot_content (str): The DOT content to render into an SVG file.
        output_dir (Path): The directory where the SVG file will be saved.
    """
    svg_file = output_dir / Path('commands.svg')
    logging.info(f'Rendering SVG to: {svg_file}')
    source = Source(dot_content)
    source.render(svg_file.with_suffix(''), format='svg', cleanup=True)


def render_jpg(dot_content: str, output_dir: Path) -> None:
    """Render the DOT content to a JPG file.

    Args:
        dot_content (str): The DOT content to render into a JPG file.
        output_dir (Path): The directory where the JPG file will be saved.
    """
    jpg_file = output_dir / Path('commands.jpg')
    logging.info(f'Rendering JPG to: {jpg_file}')
    source = Source(dot_content)
    source.render(jpg_file.with_suffix(''), format='jpg', cleanup=True)


def write_files(dot_content: str, output_dir: Path) -> None:
    """Write the DOT file, SVG, and JPG files to the output directory.

    Args:
        dot_content (str): The DOT content to write to the files.
        output_dir (Path): The directory where the files will be saved.
    """
    write_dot_file(dot_content, output_dir)
    render_svg(dot_content, output_dir)
    render_jpg(dot_content, output_dir)


def process(output_dir: Path) -> None:
    """Produce the files.

    Args:
        output_dir (Path): The directory where the files will be saved.
    """
    dot_content = generate_dot_content()
    write_files(dot_content, output_dir)


def main() -> None:
    """Document Commands."""
    parser = create_arg_parser()
    args = parser.parse_args()
    output_dir: Path = args.output
    try:
        validate_output_directory(output_dir)
    except DirectoryValidationError as dve:
        logging.error(f'Error validating output directory: {dve}')
        sys.exit(1)
    load_modules('src.commands')
    try:
        validate_commands()
    except CommandValidationError as cve:
        logging.error(f'Error validating commands: {cve}')
        sys.exit(1)
    process(output_dir)


if __name__ == '__main__':
    setup_logging()
    logging.info('Starting DOT file generation.')
    main()
    logging.info('DOT file generation completed successfully.')
    sys.exit(0)
