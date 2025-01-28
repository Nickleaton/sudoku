import argparse
import logging
import sys
from pathlib import Path

from graphviz import Source  # For converting DOT to other formats
from jinja2 import Template

from src.commands.command import Command  # Ensure this is where your Command class is defined
from src.utils.load_modules import load_modules

# Define the Jinja2 template
template_string = """
digraph {
    rankdir=TB;
    node [shape=box];
    {% for cls_name, class_type in classes.items() %}
        {% for precondition in class_type().preconditions %}
            "{{ class_type().name }}" -> "{{ precondition().name }}";
        {% endfor %}
    {% endfor %}
}
"""


def create_arg_parser() -> argparse.ArgumentParser:
    """Creates an argument parser for command-line arguments.

    Returns:
        argparse.ArgumentParser: The argument parser instance.
    """
    parser = argparse.ArgumentParser(description='Generate DOT, SVG, and JPG files for command dependencies.')
    parser.add_argument(
        'output',
        type=Path,
        help='The output directory for the generated files.'
    )
    return parser


def setup_logging() -> None:
    """Sets up logging for the script."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
    )


def generate_dot_content() -> str:
    """Generates the DOT content using the Jinja2 template and Command.classes.

    Returns:
        str: The rendered DOT content.
    """
    logging.info('Rendering DOT content...')
    template = Template(template_string)
    return template.render(classes=Command.classes)


def write_dot_file(dot_content: str, output_dir: Path) -> None:
    """Writes the DOT content to a file.

    Args:
        dot_content (str): The DOT content to write.
        output_dir (Path): The directory to write the file.
    """
    dot_file = output_dir / 'commands.dot'
    logging.info(f'Writing DOT file to: {dot_file}')
    with dot_file.open('w') as f:
        f.write(dot_content)


def render_svg(dot_content: str, output_dir: Path) -> None:
    """Renders the DOT content to an SVG file.

    Args:
        dot_content (str): The DOT content to render.
        output_dir (Path): The directory to write the SVG file.
    """
    svg_file = output_dir / 'commands.svg'
    logging.info(f'Rendering SVG to: {svg_file}')
    source = Source(dot_content)
    source.render(svg_file.with_suffix(''), format='svg', cleanup=True)


def render_jpg(dot_content: str, output_dir: Path) -> None:
    """Renders the DOT content to a JPG file.

    Args:
        dot_content (str): The DOT content to render.
        output_dir (Path): The directory to write the JPG file.
    """
    jpg_file = output_dir / 'commands.jpg'
    logging.info(f'Rendering JPG to: {jpg_file}')
    source = Source(dot_content)
    source.render(jpg_file.with_suffix(''), format='jpg', cleanup=True)


def main() -> None:
    """Main entry location for the script."""
    setup_logging()
    logging.info('Starting DOT file generation.')

    # Parse arguments
    parser = create_arg_parser()
    args = parser.parse_args()

    # Ensure the output directory exists
    output_dir: Path = args.output
    if not output_dir.exists():
        logging.info(f'Creating output directory: {output_dir}')
        output_dir.mkdir(parents=True, exist_ok=True)

    if not output_dir.is_dir():
        logging.error(f'The specified output path is not a directory: {output_dir}')
        sys.exit(1)

    # Load command modules to populate Command.classes
    logging.info('Loading command modules...')
    load_modules('src.commands')

    # Check if Command.classes is populated
    if not Command.classes:
        logging.error('No commands found in Command.classes. Ensure modules are loaded correctly.')
        sys.exit(1)

    # Generate DOT content
    dot_content = generate_dot_content()

    # Write files
    write_dot_file(dot_content, output_dir)
    render_svg(dot_content, output_dir)
    render_jpg(dot_content, output_dir)

    logging.info('DOT file generation completed successfully.')
    sys.exit(0)


if __name__ == '__main__':
    main()
