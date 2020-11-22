import numpy as np

from hypothesis import given
from hypothesis.strategies import integers, lists, booleans
from hypothesis.strategies import composite, permutations

from exact_cover_np import get_exact_cover


@composite
def exact_cover_problem(draw):
    width = draw(integers(min_value=1, max_value=15))
    data = draw(lists(lists(booleans(), min_size=width, max_size=width), min_size=1, max_size=30))
    return np.array(data, dtype=np.int32)


@given(exact_cover_problem())
def test_exact_cover(array_data):
    rowcount = len(array_data)
    actual = get_exact_cover(array_data)
    assert actual.size <= rowcount
    assert all(actual < rowcount)


@composite
def array_with_exact_cover(draw):
    width = draw(integers(min_value=1, max_value=15))
    dummy_data = draw(lists(lists(booleans(), min_size=width, max_size=width), min_size=1, max_size=30))
    cover_size = draw(integers(min_value=1, max_value=10))
    cover = draw(lists(integers(min_value=0, max_value=cover_size - 1), min_size=width, max_size=width))
    cover_data = [[a == i for a in cover] for i in range(0, cover_size)]
    data = cover_data + dummy_data
    shuffled_data = draw(permutations(data))
    return np.array(shuffled_data, dtype=np.int32)


@given(array_with_exact_cover())
def test_exact_cover_with_solution(array_data):
    rowcount = len(array_data)
    actual = get_exact_cover(array_data)
    assert actual.size > 0
    assert actual.size <= rowcount
    assert all(actual < rowcount)
    check_cover = array_data[actual, :].sum(axis=0)
    assert all(check_cover == 1)


@composite
def exact_cover_problem_with_empty_col(draw):
    width = draw(integers(min_value=1, max_value=15))
    data = draw(lists(lists(booleans(), min_size=width, max_size=width), min_size=1, max_size=30))
    array = np.array(data, dtype=np.int32)
    col = draw(integers(min_value=0, max_value=width-1))
    array[:, col] = 0
    return array


@given(exact_cover_problem_with_empty_col())
def test_exact_cover_without_solution(array_data):
    rowcount = len(array_data)
    actual = get_exact_cover(array_data)
    assert actual.size == 0
