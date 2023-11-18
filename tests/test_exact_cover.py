import numpy as np
import pytest

from hypothesis import given
from hypothesis.strategies import sampled_from

from exact_cover import get_exact_cover
from exact_cover.error import NoSolution
from exact_cover.io import DTYPE_FOR_ARRAY
from .helpers.polyomino_data import polyomino_problem
from .test_exact_cover_problems import large_problems_without_solution


def test_exact_cover():
    data = np.array([[1, 0, 0], [0, 1, 0], [0, 1, 1], [0, 0, 1]], dtype=DTYPE_FOR_ARRAY)
    expected = np.array([0, 1, 3])
    actual = get_exact_cover(data)
    np.testing.assert_array_equal(actual, expected)


def test_exact_cover_with_0_rows():
    data = np.array([[1, 0, 0], [0, 0, 0], [0, 1, 0], [0, 1, 1], [0, 0, 0], [0, 0, 1]], dtype=DTYPE_FOR_ARRAY)
    expected = np.array([0, 2, 5])
    actual = get_exact_cover(data)
    np.testing.assert_array_equal(actual, expected)


def test_exact_cover_c_order_array():
    data = np.array(
        [[1, 0, 0], [0, 1, 0], [0, 1, 1], [0, 0, 1]], dtype=DTYPE_FOR_ARRAY, order="C"
    )
    expected = np.array([0, 1, 3])
    actual = get_exact_cover(data)
    np.testing.assert_array_equal(actual, expected)


def test_exact_cover_fortran_order_array():
    data = np.array(
        [[1, 0, 0], [0, 1, 0], [0, 1, 1], [0, 0, 1]], dtype=DTYPE_FOR_ARRAY, order="F"
    )
    expected = np.array([0, 1, 3])
    actual = get_exact_cover(data)
    np.testing.assert_array_equal(actual, expected)


def test_exact_cover_read_from_file():
    data = np.load("tests/files/tiny_cover_problem.npy")
    expected = np.array([0, 1, 3])
    actual = get_exact_cover(data)
    np.testing.assert_array_equal(actual, expected)


@given(sampled_from([np.int32, np.int8, np.bool_, None, DTYPE_FOR_ARRAY]))
def test_exact_cover_different_dtypes(dtype):
    """
    Check the exact cover routine works when input array has different dtypes
    """
    data = np.array([[1, 0, 0], [0, 1, 0], [0, 1, 1], [0, 0, 1]], dtype=dtype)
    expected = np.array([0, 1, 3])
    actual = get_exact_cover(data)
    np.testing.assert_array_equal(actual, expected)


def test_exact_cover_no_solution():
    data = np.array([[1, 0, 0], [0, 1, 0], [0, 1, 0], [0, 0, 0]], dtype=DTYPE_FOR_ARRAY)
    with pytest.raises(NoSolution):
        get_exact_cover(data)


def test_simple_exact_cover():
    """
    ArthurKantor's 1st test case
    """
    data = np.array([[1, 0, 0], [0, 1, 1]], dtype=DTYPE_FOR_ARRAY)
    expected = np.array([0, 1])
    actual = get_exact_cover(data)
    np.testing.assert_array_equal(actual, expected)


def test_single_row_exact_cover():
    """
    ArthurKantor's 2nd test case
    """
    data = np.array([[1, 1, 1]], dtype=DTYPE_FOR_ARRAY)
    expected = np.array([0])
    actual = get_exact_cover(data)
    np.testing.assert_array_equal(actual, expected)


def test_complex_exact_cover_problem():
    data = np.array(polyomino_problem, dtype=DTYPE_FOR_ARRAY)
    actual = get_exact_cover(data)
    assert actual.shape == (13,)


@given(large_problems_without_solution)
def test_no_solution(data):
    with pytest.raises(NoSolution):
        get_exact_cover(data)
