import numpy as np
import pytest

from hypothesis import given

from exact_cover import get_exact_cover
from exact_cover.error import NoSolution
from .helpers.polyomino_data import polyomino_problem
from .test_exact_cover_problems import large_problems_without_solution


def test_exact_cover():
    data = np.array([[1, 0, 0], [0, 1, 0], [0, 1, 1], [0, 0, 1]], dtype=np.int32)
    expected = np.array([0, 1, 3])
    actual = get_exact_cover(data)
    np.testing.assert_array_equal(actual, expected)


def test_exact_cover_no_solution():
    data = np.array([[1, 0, 0], [0, 1, 0], [0, 1, 0], [0, 0, 0]], dtype=np.int32)
    with pytest.raises(NoSolution):
        get_exact_cover(data)


def test_simple_exact_cover():
    """
    ArthurKantor's 1st test case
    """
    data = np.array([[1, 0, 0], [0, 1, 1]], dtype=np.int32)
    expected = np.array([0, 1])
    actual = get_exact_cover(data)
    np.testing.assert_array_equal(actual, expected)


def test_single_row_exact_cover():
    """
    ArthurKantor's 2nd test case
    """
    data = np.array([[1, 1, 1]], dtype=np.int32)
    expected = np.array([0])
    actual = get_exact_cover(data)
    np.testing.assert_array_equal(actual, expected)


def test_complex_exact_cover_problem():
    data = np.array(polyomino_problem, dtype=np.int32)
    actual = get_exact_cover(data)
    assert actual.shape == (13,)


@given(large_problems_without_solution)
def test_no_solution(data):
    with pytest.raises(NoSolution):
        get_exact_cover(data)
