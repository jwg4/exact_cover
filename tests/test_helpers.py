import numpy as np

from exact_cover.helpers import reduce, split_problem


def test_reduce():
    d = [[0, 1, 0], [1, 1, 1], [1, 1, 1]]
    a = np.array(d)
    result = reduce(a)
    np.testing.assert_array_equal(result, a)


def test_split_problem():
    d = [[0, 1, 0], [1, 1, 1], [1, 1, 1]]
    a = np.array(d)
    result = list(split_problem(a, 2))
    assert len(result) >= 2
    for sub in result:
        assert isinstance(sub, np.ndarray)
        assert sub.shape == (1, 3)
