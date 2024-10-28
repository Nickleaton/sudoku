from pathlib import Path

import pytest
from strictyaml import load

from generated_config_schema2 import problem_schema
#from config_schema import problem_schema


@pytest.mark.parametrize("yaml_file", list(Path("problems/easy").glob("*.yaml")))
def test_yaml_files(yaml_file):
    """Test to validate each YAML file against a strictyaml schema"""
    print(yaml_file)
    with yaml_file.open() as f:
        yaml_content = f.read()
    parsed_yaml = load(yaml_content, problem_schema)
    assert parsed_yaml is not None, f"Failed to load YAML file: {yaml_file.name}"


if __name__ == "__main__":
    pytest.main()
