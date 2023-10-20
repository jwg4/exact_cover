import doctest
import sys

import pytest

from tests.config import GLOBAL_CONFIG  # noqa: F401


def test():
    ret = pytest.main()
    sys.exit(ret)


def quicktest():
    global GLOBAL_CONFIG
    GLOBAL_CONFIG["SKIP_SLOW"] = True
    ret = pytest.main(["--fail-slow", "2s"])
    sys.exit(ret)


def run_doctest():
    doctest.testfile("../README.md", raise_on_error=True)
    doctest.testfile("../examples.md", raise_on_error=True)
