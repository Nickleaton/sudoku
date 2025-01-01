from pathlib import Path


def process(path: Path, comment: str) -> None:
    with open(path / Path("__init__.py"), 'w') as f:
        f.write(f"# {comment}\n\n")
        for file in path.glob(pattern="*.py"):
            f.write(f"import src.vectors.{file.name[:-3]}\n")


process(Path(r"src\items"), "Module that handles constraints.")