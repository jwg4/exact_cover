import doctest

import pytest

from tests.config import GLOBAL_CONFIG  # noqa: F401


def test():
    pytest.main()


def quicktest():
    global GLOBAL_CONFIG
    GLOBAL_CONFIG["SKIP_SLOW"] = True
    pytest.main(["--fail-slow", "2s"])


def run_doctest():
    doctest.testfile("../README.md")
