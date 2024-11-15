from pathlib import Path
from strictyaml import load, YAMLParseError
from generated_config_schema2 import problem_schema


def validate_yaml_file(yaml_file: Path):
    """Validate a YAML file against the strictyaml schema."""
    try:
        with yaml_file.open() as f:
            yaml_content = f.read()
        parsed_yaml = load(yaml_content, problem_schema)
        if parsed_yaml is None:
            raise ValueError(f"Failed to load YAML file: {yaml_file.name}")
    except YAMLParseError as e:
        raise ValueError(f"Failed to parse YAML file {yaml_file.name}: {e}") from e
    except Exception as e:
        raise ValueError(f"Unexpected error with YAML file {yaml_file.name}: {e}") from e


if __name__ == "__main__":
    validate_yaml_file(Path('problems/easy/problem001.yaml'))
