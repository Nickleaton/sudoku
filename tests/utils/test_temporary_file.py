import unittest
from pathlib import Path

from src.utils.config import Config
from src.utils.temporary_file import TemporaryFile

config = Config()


class TestTemporaryFile(unittest.TestCase):

    def test_create(self):
        config.reload()
        config.temporary_directory = Path(config.temporary_directory) / Path("non_existing_subdir")
        if config.temporary_directory.exists():
            config.temporary_directory.rmdir()
        # noinspection PyBroadException
        try:
            with TemporaryFile() as tf:
                self.assertFalse(tf.name.exists())
                with open(tf.name, 'w') as f:
                    f.write('Hello world')
                self.assertTrue(tf.name.exists())
            self.assertFalse(tf.name.exists())
            if config.temporary_directory.exists():
                config.temporary_directory.rmdir()
        except Exception:
            pass
        finally:
            config.reload()


    def test_bad_config(self):
        config.reload()
        # noinspection PyBroadException
        try:
            save = config.temporary_directory
            config.temporary_directory = []
            with self.assertRaises(ValueError):
                _ = TemporaryFile()
            config.temporary_directory = save
        except Exception:
            pass
        finally:
            config.reload()


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
