import numpy as np

from exact_cover.helpers import reduce


def test_reduce():
    d = [[0, 1, 0], [1, 1, 1], [1, 1, 1]]
    a = np.array(d)
    result = reduce(a)
    np.testing.assert_array_equal(result, a)
