import numpy as np
import pytest

from hypothesis import given
from hypothesis.strategies import sampled_from

from exact_cover_impl import get_solution_count
from exact_cover.error import NoSolution
from exact_cover.io import DTYPE_FOR_ARRAY
from .helpers.polyomino_data import polyomino_problem
from .test_exact_cover_problems import large_problems_without_solution


def test_exact_cover():
    data = np.array([[1, 0, 0], [0, 1, 0], [0, 1, 1], [0, 0, 1]], dtype=DTYPE_FOR_ARRAY)
    result = get_solution_count(data)
    assert result == 2


def test_exact_cover_c_order_array():
    data = np.array(
        [[1, 0, 0], [0, 1, 0], [0, 1, 1], [0, 0, 1]], dtype=DTYPE_FOR_ARRAY, order="C"
    )
    result = get_solution_count(data)
    assert result == 2


def test_exact_cover_fortran_order_array():
    data = np.array(
        [[1, 0, 0], [0, 1, 0], [0, 1, 1], [0, 0, 1]], dtype=DTYPE_FOR_ARRAY, order="F"
    )
    result = get_solution_count(data)
    assert result == 2


def test_exact_cover_read_from_file():
    data = np.load("tests/files/tiny_cover_problem.npy")
    result = get_solution_count(data)
    assert result == 2


@given(sampled_from([np.int32, np.int8, np.bool_, None, DTYPE_FOR_ARRAY]))
def test_exact_cover_different_dtypes(dtype):
    """
    Check the exact cover routine works when input array has different dtypes
    """
    data = np.array([[1, 0, 0], [0, 1, 0], [0, 1, 1], [0, 0, 1]], dtype=dtype)
    result = get_solution_count(data)
    assert result == 2


def test_exact_cover_no_solution():
    data = np.array([[1, 0, 0], [0, 1, 0], [0, 1, 0], [0, 0, 0]], dtype=DTYPE_FOR_ARRAY)
    result = get_solution_count(data)
    assert result == 0


def test_simple_solution_count():
    """
    ArthurKantor's 1st test case
    """
    data = np.array([[1, 0, 0], [0, 1, 1]], dtype=DTYPE_FOR_ARRAY)
    result = get_solution_count(data)
    assert result == 1


def test_single_row_exact_cover():
    """
    ArthurKantor's 2nd test case
    """
    data = np.array([[1, 1, 1]], dtype=DTYPE_FOR_ARRAY)
    result = get_solution_count(data)
    assert result == 1


def test_complex_exact_cover_problem():
    data = np.array(polyomino_problem, dtype=DTYPE_FOR_ARRAY)
    result = get_solution_count(data)
    assert result == 1


@given(large_problems_without_solution)
def test_no_solution(data):
    result = get_solution_count(data)
    assert result == 0
