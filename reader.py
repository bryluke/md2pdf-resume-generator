import os
from exceptions import FileNotFoundError as ResumeFileNotFoundError


def read_markdown(path: str) -> str:
    """Read markdown content from file."""
    if not os.path.exists(path):
        raise ResumeFileNotFoundError(f"Markdown file not found: {path}")

    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        raise ResumeFileNotFoundError(f"Failed to read markdown file: {e}")


def read_template(path: str) -> str:
    """Read HTML template from file."""
    if not os.path.exists(path):
        raise ResumeFileNotFoundError(f"Template file not found: {path}")

    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        raise ResumeFileNotFoundError(f"Failed to read template file: {e}")
