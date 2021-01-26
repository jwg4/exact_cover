import numpy as np

from exact_cover import get_exact_cover
from .helpers.polyomino_data import polyomino_problem


def test_exact_cover():
    data = np.array(
        [[1, 0, 0], [0, 1, 0], [0, 1, 1], [0, 0, 1]],
        dtype=np.int32
    )
    expected = np.array([0, 1, 3])
    actual = get_exact_cover(data)
    np.testing.assert_array_equal(actual, expected)


def test_exact_cover_no_solution():
    data = np.array(
        [[1, 0, 0], [0, 1, 0], [0, 1, 0], [0, 0, 0]],
        dtype=np.int32
    )
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


def test_complex_exact_cover_problem():
    data = np.array(polyomino_problem, dtype=np.int32)
    actual = get_exact_cover(data)
    assert actual.shape == (13, )


def test_no_solution():
    data = np.genfromtxt(
        "tests/files/cylinder.csv",
        dtype=np.int32, delimiter=","
    )
    assert data.shape == (644, 208)
    actual = get_exact_cover(data)
    assert actual.shape == (0, )


def test_reduced_no_solution():
    data = np.genfromtxt("tests/files/reduced.csv", dtype=np.int32)
    assert data.shape == (2, 60)
    actual = get_exact_cover(data)
    assert actual.shape == (0, )


def test_part_reduced_no_solution():
    data = np.genfromtxt("tests/files/part_reduced.csv", dtype=np.int32)
    assert data.shape == (478, 172)
    actual = get_exact_cover(data)
    assert actual.shape == (0, )
