import numpy as np

from hypothesis import given

from exact_cover.helpers import reduce, split_problem
from exact_cover.error import NoSolution, CannotSplitFurther

from .test_exact_cover_problems import (
    all_problems,
    array_with_solution,
    array_without_solution,
)


def test_reduce():
    d = [[0, 1, 0], [1, 1, 1], [1, 1, 1]]
    a = np.array(d)
    result = reduce(a)
    np.testing.assert_array_equal(result, a)


@given(array_with_solution)
def test_reduce_with_solution(a):
    result = reduce(a)
    assert result.shape[0] <= a.shape[0]
    assert result.shape[1] <= a.shape[1]


@given(array_without_solution)
def test_reduce_without_solution(a):
    try:
        result = reduce(a)
        assert result.shape[0] <= a.shape[0]
        assert result.shape[1] <= a.shape[1]
    except NoSolution:
        assert True


def test_split_problem():
    d = [[0, 1, 0], [1, 1, 1], [1, 1, 1]]
    a = np.array(d)
    result = list(split_problem(a, 2))
    assert len(result) >= 2
    for sub in result:
        assert isinstance(sub, np.ndarray)
        assert sub.shape == (1, 3)


@given(all_problems)
def test_split_arbitrary_problem(a):
    result = list(split_problem(a, 2))
    try:
        assert len(result) >= 2
        x, y = a.shape
        for sub in result:
            assert isinstance(sub, np.ndarray)
            x_1, y_1 = sub.shape
            assert x_1 < x
            assert y_1 == y
    except NoSolution:
        assert True
    except CannotSplitFurther:
        assert True
