""" Base class for simple commands"""
from typing import Any

from src.commands.command import Command


class SimpleCommand(Command):

    def __init__(self):
        """ Create the simple command """
        super().__init__()
    #     self.__dict__['output'] = {}
    #
    # def __getattr__(self, key: str) -> Any:
    #     return self.output[key]
    #
    # def __setattr__(self, key: str, value: Any):
    #     self.output[key] = value
