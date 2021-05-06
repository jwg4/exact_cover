import doctest

import pytest


def test():
    pytest.main()


def run_doctest():
    doctest.testfile("../README.md")
