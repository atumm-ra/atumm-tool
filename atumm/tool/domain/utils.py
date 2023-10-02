from typing import List
import os
from pathlib import Path


def create_module(module_path: str, files: List=[]):
    """
    Create a new Python module at the given module path.
    """
    current_path = ""
    for module in module_path.split("/"):
        current_path = os.path.join(current_path, module)
        Path(current_path).mkdir(parents=True, exist_ok=True)
        Path(current_path, "__init__.py").touch()

    for file in files:
        Path(current_path, file).touch()
