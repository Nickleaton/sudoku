"""Script to generate documentation."""
import argparse
import logging
import logging.config
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from src.items.item import Item
from src.utils.config import Config
from src.utils.load_modules import load_modules

config: Config = Config()
logging.config.dictConfig(Config().get_dict('logging'))
logger = logging.getLogger("generate_documentation")

env = Environment(loader=FileSystemLoader(Path('src/templates')), autoescape=True)


def process_file(clazz: type[Item], file_path: Path, template_name: str) -> None:
    """Create Documentation.

    Args:
        clazz (type[Item]): The class to generate documentation for.
        file_path (Path): The file path to write the documentation to.
        template_name (str): The name of the template to use.

    Returns:
        None
    """
    logging.info(f"Processing {clazz.__name__} -> {file_path}")
    if not file_path.parent.exists():
        file_path.parent.mkdir(parents=True, exist_ok=True)
    template = env.get_template(template_name)
    info: dict[str, str] = clazz.get_info()
    output: str = template.render(info=info)
    file_path.write_text(output, encoding='utf-8')


def document(target_directory: Path) -> None:
    """Create Documentation.

    Args:
        target_directory (Path): The directory to write the documentation to.

    Returns:
        None
    """
    name: str
    clazz: type[Item]
    for name, clazz in Item.classes.items():
        if name == 'Solution':
            continue
        file_path: Path = target_directory / Path('rst') / (name + '.rst')
        process_file(clazz, file_path, 'documentation.rst')
        file_path: Path = target_directory / Path('md') / (name + '.md')
        process_file(clazz, file_path, 'documentation.md')


def create_arg_parser() -> argparse.ArgumentParser:
    """Create the argument parser.

    Returns:
        argparse.ArgumentParser
    """
    parser = argparse.ArgumentParser(description='Generate documentation.')
    parser.add_argument('--target', type=Path, help='Target directory for generated documentation')
    parser.add_argument('--source', type=Path, help='Source directory for generated documentation')
    return parser


def main() -> None:
    """Main function to generate documentation.

    Returns:
        None
    """
    logging.info("Creating documentation...")
    parser: argparse.ArgumentParser = create_arg_parser()
    args: argparse.Namespace = parser.parse_args()

    logging.info("Loading modules...")
    load_modules('src.items')

    if not args.target.exists():
        logging.info(f"Creating target directory: {args.target}")
        args.target.mkdir(parents=True, exist_ok=True)

    document(args.target)

    logging.info("Documentation generated.")
    sys.exit(0)


if __name__ == '__main__':
    """Generate documentation."""
    main()
