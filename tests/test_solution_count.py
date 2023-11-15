import numpy as np

from exact_cover_impl import get_solution_count
from exact_cover.io import DTYPE_FOR_ARRAY


def test_solution_count():
    data = np.array([[1, 0, 0], [0, 1, 0], [0, 1, 1], [0, 0, 1]], dtype=DTYPE_FOR_ARRAY)
    result = get_solution_count(data)
    assert result == 2


def test_solution_count_single_solution():
    data = np.array([[1, 0, 0], [0, 1, 0], [0, 1, 1]], dtype=DTYPE_FOR_ARRAY)
    result = get_solution_count(data)
    assert result == 1


def test_solution_count_no_solutions():
    data = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0]], dtype=DTYPE_FOR_ARRAY)
    result = get_solution_count(data)
    assert result == 0
