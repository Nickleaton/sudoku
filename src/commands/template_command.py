""" Command that takes a jinja2 template that produces and output string and writes it to a file """
import logging
from pathlib import Path

import jinja2

from src.commands.simple_command import SimpleCommand


class TemplateCommand(SimpleCommand):
    """ Create a file from the outputs using a jinja2 template"""

    def __init__(self, template_file_name: Path):
        """ Create the template command

        :param template_file_name: name of template file
        """
        super().__init__()
        self.template_file_name = template_file_name
        logging.info(f"Loading template {self.template_file_name}")
        self.template = jinja2.Template(open(self.template_file_name).read())
        self.output = None

    def execute(self) -> None:
        """ Produce the file """
        super().execute()
        self.output = self.template.render(self.parent.__dict__)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({repr(self.file_name)}, {repr(self.template_file_name)}"
