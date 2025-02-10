"""load_modules."""
import importlib
import pkgutil


def load_modules(package_name: str, subpackage: str | None = None) -> None:
    """Dynamically loads all modules within the specified package or subpackage.

    Args:
        package_name (str): The name of the package to load modules from.
        subpackage (str | None): If provided, it will load modules from the subpackage within the package.

    Raises:
        ModuleNotFoundError: If the specified package or subpackage is not found.
    """
    full_package_name: str = f'{package_name}.{subpackage}' if subpackage else package_name

    try:
        package = importlib.import_module(full_package_name)
    except ModuleNotFoundError as exp:
        raise ModuleNotFoundError(f'Could not find the package or subpackage {full_package_name!r}.') from exp

    # Find all modules in the package or subpackage
    for _, module_name, _ in pkgutil.iter_modules(package.__path__):
        # Import each module dynamically
        importlib.import_module(f'{full_package_name}.{module_name}')
