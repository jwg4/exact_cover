import numpy as np
import pytest

from hypothesis import given
from hypothesis.strategies import sampled_from

from exact_cover import get_all_solutions
from exact_cover.error import NoSolution
from exact_cover.io import DTYPE_FOR_ARRAY
from .helpers.polyomino_data import polyomino_problem
from .test_exact_cover_problems import large_problems_without_solution


def test_exact_cover():
    data = np.array([[1, 0, 0], [0, 1, 0], [0, 1, 1], [0, 0, 1]], dtype=DTYPE_FOR_ARRAY)
    expected = np.array([[0, 1, 3], [0, 2, 0]])
    actual = get_all_solutions(data)
    np.testing.assert_array_equal(actual, expected)


def test_max_solutions():
    data = np.array([[1, 0, 0], [0, 1, 0], [0, 1, 1], [0, 0, 1]], dtype=DTYPE_FOR_ARRAY)
    expected = np.array([[0, 1, 3]])
    actual = get_all_solutions(data, 1)
    np.testing.assert_array_equal(actual, expected)
