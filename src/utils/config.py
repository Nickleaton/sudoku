from pathlib import Path
from typing import Any

import oyaml as yaml
from pydotted import pydot


class Config:
    __instance = None

    def __new__(cls, config_file_path: Path):
        if cls.__instance is None:
            cls.__instance = super(Config, cls).__new__(cls)
            cls.__instance.__initialized = False
        cls.__instance.config_file_path = config_file_path
        return cls.__instance

    def __init__(self, config_file_path: Path):
        if self.__initialized:
            return
        self.__initialized = True
        with open(self.config_file_path) as file:
            self.config = pydot(yaml.load(file, Loader=yaml.SafeLoader))

    def __getattr__(self, key: str) -> Any:
        return self.config[key]


# config = Config(Path("config.yaml"))
#
# print(config.drawing.size)
