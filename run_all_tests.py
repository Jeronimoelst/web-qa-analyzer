from pathlib import Path

import pytest


if __name__ == "__main__":
    tests_path = Path(__file__).parent / "tests"
    raise SystemExit(pytest.main(["-v", str(tests_path)]))
