from tempfile import mkstemp

from numpy.testing import assert_array_equal

from exact_cover.helpers import create_numpy_array
from exact_cover.io import load_problem, save_problem


def test_basic_roundtrip():
    _, filename = mkstemp()
    array = create_numpy_array([[0, 1, 0], [1, 0, 1]])
    save_problem(filename, array)
    problem = load_problem(filename)
    assert_array_equal(array, problem)
