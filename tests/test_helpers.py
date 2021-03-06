import numpy as np

from hypothesis import given, settings
from hypothesis.strategies import integers

from exact_cover import get_exact_cover
from exact_cover.helpers import reduce, split_problem, is_solution
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
        assert sub.shape == a.shape


@given(all_problems)
@settings(deadline=None)
def test_split_arbitrary_problem(a):
    try:
        result = list(split_problem(a, 2))
        assert len(result) >= 2
        for sub in result:
            assert isinstance(sub, np.ndarray)
            assert sub.shape == a.shape
    except NoSolution:
        assert True
    except CannotSplitFurther:
        assert True


@given(all_problems, integers(2, 30))
@settings(deadline=None)
def test_correct_number_of_splits(a, n):
    try:
        result = list(split_problem(a, n))
        assert len(result) >= n
        assert len(result) < n * a.shape[0]
    except NoSolution:
        assert True
    except CannotSplitFurther:
        assert True


@given(all_problems, integers(2, 30))
@settings(deadline=None)
def test_solution_to_split_problem_solves_original_problem(a, n):
    try:
        result = list(split_problem(a, n))
        for sub in result:
            s = get_exact_cover(sub)
            if s.size > 0:
                assert is_solution(s, sub)
                assert is_solution(s, a)
    except NoSolution:
        assert True
    except CannotSplitFurther:
        assert True


@given(array_with_solution)
def test_is_solution(a):
    s = get_exact_cover(a)
    assert is_solution(s, a)


@given(array_with_solution)
def test_is_solution_fails_for_proper_subset(a):
    s = get_exact_cover(a)
    assert not is_solution(s[:-1], a)
