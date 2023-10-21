import numpy as np

from exact_cover import get_exact_cover


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
