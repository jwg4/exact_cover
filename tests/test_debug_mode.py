import numpy as np

from exact_cover import get_exact_cover


def test_exact_cover_default():
    data = np.array([[1, 0, 0], [0, 1, 0], [0, 1, 1], [0, 0, 1]], dtype=np.int32)
    expected = np.array([0, 1, 3])
    actual = get_exact_cover(data)
    np.testing.assert_array_equal(actual, expected)


def test_exact_cover_false():
    data = np.array([[1, 0, 0], [0, 1, 0], [0, 1, 1], [0, 0, 1]], dtype=np.int32)
    expected = np.array([0, 1, 3])
    actual = get_exact_cover(data, False)
    np.testing.assert_array_equal(actual, expected)


def test_exact_cover_true():
    data = np.array([[1, 0, 0], [0, 1, 0], [0, 1, 1], [0, 0, 1]], dtype=np.int32)
    expected = np.array([0, 1, 3])
    actual, debug_info = get_exact_cover(data, True)
    np.testing.assert_array_equal(actual, expected)
