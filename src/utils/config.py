""" Config: A singleton class representing the configuration of an application. """
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
    """
    __instance = None

    def __new__(cls, config_file_path: Path = Path("config.yaml")):
        """
        Creates a new instance of the `Config` class if one doesn't already exist.

        Args:
            config_file_path (Path): The path to the YAML configuration file.

        Returns:
            Config: The singleton instance of the `Config` class.
        """
        if cls.__instance is None:
            cls.__instance = super(Config, cls).__new__(cls)
            cls.__instance.__initialized = False
        cls.__instance.config_file_path = config_file_path
        return cls.__instance

    def __init__(self):
        """
        Initializes the `Config` class instance and reads the YAML configuration file.
        """
        if self.__initialized:
            return
        self.__initialized = True
        with open(self.config_file_path) as file:
            self.config = pydot(yaml.load(file, Loader=yaml.SafeLoader))

    def __getattr__(self, key: str) -> Any:
        """
        Retrieves the value of a configuration parameter from the config
        You can use dotted attribute access

        Args:
            key (str): The name of the configuration parameter to retrieve.

        Returns:
            Any: The value of the configuration parameter.
        """
        return self.config[key]

