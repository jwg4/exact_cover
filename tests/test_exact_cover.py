import numpy as np

from pytest import mark

from exact_cover_np import get_exact_cover


def test_exact_cover():
    data = np.array([[1, 0, 0], [0, 1, 0], [0, 1, 1], [0, 0, 1]], dtype=np.int32)
    expected = np.array([0, 1, 3])
    actual = get_exact_cover(data)
    np.testing.assert_array_equal(actual, expected)


def test_exact_cover_no_solution():
    data = np.array([[1, 0, 0], [0, 1, 0], [0, 1, 0], [0, 0, 0]], dtype=np.int32)
    expected = np.array([])
    actual = get_exact_cover(data)
    np.testing.assert_array_equal(actual, expected)


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
