"""Config."""
import threading
from pathlib import Path
from typing import Any

import oyaml as yaml
from pydotted import pydot


class Config:
    """A singleton class representing the configuration of an application."""

    _instance: 'Config' | None = None
    _lock: threading.Lock = threading.Lock()

    def __new__(cls, config_file_path: Path | None = None) -> 'Config':
        """Create a new instance of the `Config` class if one doesn't already exist.

        Args:
            config_file_path (Path | None): The config_file path to the YAML configuration file.

        Returns:
            Config: The singleton instance of the `Config` class.

        Raises:
            ValueError: If a Config instance already exists with a different config_file_path.
        """
        if config_file_path is None:
            config_file_path = Path('config.yaml')

        with cls._lock:  # Acquire the lock before proceeding
            if cls._instance is None:
                cls._instance = super().__new__(cls)

                cls._instance.initialized = False
                cls._instance.config_file_path = config_file_path
            elif cls._instance.config_file_path != config_file_path:
                raise ValueError('Config instance already created with a different config_file_path.')
        return cls._instance

    def __init__(self):
        """Initialize the `Config` class instance and read the YAML configuration file."""
        if getattr(self, 'initialized', False):
            return
        self.initialized = True  # Changed from __initialized to _initialized
        self.config_file_path: Path
        self.config: dict[str, Any] | None = None
        self.reload()

    def reload(self) -> None:
        """Reload the configuration from the YAML file.

        This can be used to force the configuration to be re-read from the YAML file.
        This is useful if the configuration file has changed since the application
        started.

        Raises:
            FileNotFoundError: If the configuration file is not found.
            OSError: If the configuration file is not readable.
            ValueError: If there is an error parsing the YAML file.
        """
        try:
            with self.config_file_path.open(mode='r', encoding='utf-8') as config_file:
                self.config = pydot(yaml.load(config_file, Loader=yaml.SafeLoader))
        except FileNotFoundError as exc:
            raise FileNotFoundError(f'Configuration file not found: {self.config_file_path}') from exc
        except OSError as exc:
            raise OSError(f'Configuration file not readable: {self.config_file_path}') from exc
        except yaml.YAMLError as exc:
            raise ValueError(f'Error parsing YAML file: {exc}') from exc

    def __getattr__(self, key: str) -> Any:
        """Retrieve a configuration parameter from the config using dotted attribute access.

        Args:
            key (str): The name of the configuration parameter to retrieve.

        Returns:
            Any: The input_value of the configuration parameter.

        Raises:
            AttributeError: If the configuration has not been loaded or the key does not exist.
        """
        if self.config is None:
            raise AttributeError('Configuration has not been loaded.')

        config_param: Any = self.config.get(key, None)
        if config_param is not None:
            return config_param

        raise AttributeError(f'Config object has no attribute "{key}"')

    def get_dict(self, name: str) -> dict[str, Any] | None:
        """Retrieve a dictionary from the configuration by its name.

        If the configuration has not been loaded yet, it will attempt to reload it.
        If the configuration is still not available after reloading, a ValueError is raised.

        Args:
            name (str): The name of the configuration parameter to retrieve.

        Returns:
            dict[str, Any] | None: The dictionary associated with the given name if it exists,
            or `None` if the key does not exist.

        Raises:
            ValueError: If the configuration has not been loaded and cannot be reloaded.
        """
        if self.config is None:
            self.reload()  # Try to reload the configuration
        if self.config is None:
            raise ValueError('Configuration has not been loaded.')  # If still None, raise an error
        return self.config.get(name)  # Return the dictionary or None if the key doesn't exist
