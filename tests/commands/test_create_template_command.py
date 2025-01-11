"""TestCreateTemplateCommand."""
import unittest

import pytest

from src.commands.create_template_command import CreateIndexTemplate, CreateProblemTemplate
from tests.commands.test_simple_command import TestSimpleCommand


@pytest.mark.abstract
class TestCreateTemplateCommand(TestSimpleCommand):
    """Test suite for the LoadTemplateCommand class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        self.command = None
        self.representation = None


class TestCreateIndexTemplate(TestCreateTemplateCommand):

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        self.command = CreateIndexTemplate()
        self.representation = r"CreateIndexTemplate()"


class TestCreateProblemTemplate(TestCreateTemplateCommand):

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        self.command = CreateProblemTemplate()
        self.representation = r"CreateProblemTemplate()"


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
