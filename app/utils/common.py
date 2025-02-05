import sys


def is_testing() -> bool:
    """Check if the app is running in a test environment."""
    return "pytest" in sys.modules
