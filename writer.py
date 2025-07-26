import os


def write_pdf(output_path: str) -> bool:
    """Verify PDF was written successfully."""
    if os.path.exists(output_path):
        return True
    return False
