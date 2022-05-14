import numpy as np
import pytest

from hypothesis import given

from exact_cover import get_exact_cover
from exact_cover.error import NoSolution
from .helpers.polyomino_data import polyomino_problem
from .test_exact_cover_problems import large_problems_without_solution


def test_exact_cover_debug_on():
    data = np.array([[1, 0, 0], [0, 1, 0], [0, 1, 1], [0, 0, 1]], dtype=np.int32)
    expected = np.array([0, 1, 3])
    actual = get_exact_cover(data, debug=True)
    np.testing.assert_array_equal(actual, expected)


def test_exact_cover_debug_off():
    data = np.array([[1, 0, 0], [0, 1, 0], [0, 1, 1], [0, 0, 1]], dtype=np.int32)
    expected = np.array([0, 1, 3])
    actual = get_exact_cover(data, debug=False)
    np.testing.assert_array_equal(actual, expected)
