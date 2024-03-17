import numpy as np

from exact_cover import get_all_solutions
from exact_cover.io import DTYPE_FOR_ARRAY


def test_exact_cover():
    data = np.array([[1, 0, 0], [0, 1, 0], [0, 1, 1], [0, 0, 1]], dtype=DTYPE_FOR_ARRAY)
    expected = set([(0, 1, 3), (0, 2)])
    actual = get_all_solutions(data)
    assert expected == actual


def test_max_solutions():
    data = np.array([[1, 0, 0], [0, 1, 0], [0, 1, 1], [0, 0, 1]], dtype=DTYPE_FOR_ARRAY)
    expected = set([(0, 1, 3)])
    actual = get_all_solutions(data, 1)
    np.testing.assert_array_equal(actual, expected)
