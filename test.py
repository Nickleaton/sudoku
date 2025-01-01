from pathlib import Path

import strictyaml as yaml

from src.schema.config_schema import problem_schema

# Define the directory containing your YAML files
directory = Path('problems/easy')

# Iterate over all .yaml files in the directory
for file in directory.glob('*.yaml'):
    try:
        # Read the YAML content from the file
        with open(file, 'r') as f:
            yaml_content = f.read()

        # Validate and parse the YAML content against the schema
        data = yaml.load(yaml_content, schema=problem_schema)

    except Exception as e:
        # Print the name of the file that failed validation
        print(f"File '{file.name}' failed to validate: {e}")
