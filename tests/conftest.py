import logging.config

import pytest

from src.utils.config import Config


@pytest.fixture(scope="session", autouse=True)
def configure_logging():
    logging.config.dictConfig( Config().get_dict('logging'))
