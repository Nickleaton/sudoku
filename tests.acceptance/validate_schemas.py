from pathlib import Path
import pytest
from strictyaml import load, YAMLParseError

from generated_config_schema2 import problem_schema


@pytest.mark.parametrize("yaml_file", list(Path("problems/easy").glob("*.yaml")))
def test_yaml_files(yaml_file):
    """Test to validate each YAML file against a strictyaml schema."""
    try:
        with yaml_file.open() as f:
            yaml_content = f.read()
        parsed_yaml = load(yaml_content, problem_schema)
        # We explicitly check that parsing didn't result in None (although `load` should raise an error if invalid)
        if parsed_yaml is None:
            pytest.fail(f"Failed to load YAML file: {yaml_file.name}")
    except YAMLParseError as e:
        pytest.fail(f"Failed to parse YAML file {yaml_file.name}: {e}")
    except Exception as e:
        pytest.fail(f"Unexpected error with YAML file {yaml_file.name}: {e}")


if __name__ == "__main__":
    pytest.main()
