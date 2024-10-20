""" Config: A singleton class representing the configuration of an application. """
import threading
from pathlib import Path
from typing import Any

import oyaml as yaml
from pydotted import pydot


class Config:
    """
    A singleton class representing the configuration of an application.

    Attributes:
        config_file_path (Path): The path to the YAML configuration file.
        config (pydot): A nested dictionary representing the configuration read from the YAML file.

    Examples:
        ```
        from pathlib import Path
        from config import Config

        config = Config(Path("my_config.yaml"))
        db_uri = config.database.uri
        ```
        Assuming `my_config.yaml` contains:
        ```
        database:
          uri: "postgresql://user:pass@xxyyz:9999/mydb"
        ```
    """
    __instance = None
    __lock = threading.Lock()

    def __new__(cls, config_file_path: Path = Path("config.yaml")):
        """
        Creates a new instance of the `Config` class if one doesn't already exist.

        Args:
            config_file_path (Path): The path to the YAML configuration file.

        Returns:
            Config: The singleton instance of the `Config` class.
        """
        with cls.__lock:  # Acquire the lock before proceeding
            if cls.__instance is None:
                cls.__instance = super(Config, cls).__new__(cls)
                cls.__instance.__initialized = False
                cls.__instance.config_file_path = config_file_path
            elif cls.__instance.config_file_path != config_file_path:
                raise ValueError("Config instance already created with a different config_file_path.")
        return cls.__instance

    def __init__(self):
        """
        Initializes the `Config` class instance and reads the YAML configuration file.
        """
        if self.__initialized:
            return
        self.__initialized = True
        self.config = None
        self.reload()

    def reload(self):
        """
        Reloads the configuration from the YAML file.
        Also used on construction

        This can be used to force the configuration to be re-read from the YAML file.
        This is useful if the configuration file has changed since the application
        started.
        """
        try:
            with open(self.config_file_path) as file:
                self.config = pydot(yaml.load(file, Loader=yaml.SafeLoader))
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file not found: {self.config_file_path}")
        except yaml.YAMLError as e:
            raise ValueError(f"Error parsing YAML file: {e}")

    def __getattr__(self, key: str) -> Any:
        """
        Retrieves the value of a configuration parameter from the config
        You can use dotted attribute access

        Args:
            key (str): The name of the configuration parameter to retrieve.

        Returns:
            Any: The value of the configuration parameter.
        """
        try:
            return self.config[key]
        except KeyError:
            raise AttributeError(f"'Config' object has no attribute '{key}'")
