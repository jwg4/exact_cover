import numpy as np

from hypothesis import given
from hypothesis.strategies import integers, lists, booleans
from hypothesis.strategies import composite, permutations

from exact_cover_np import get_exact_cover


@given(
    integers(min_value=0, max_value=10).flatmap(
        lambda n: lists(
            lists(booleans(), min_size=n, max_size=n), min_size=1, max_size=30
        )
    )
)
def test_exact_cover(array_data):
    rowcount = len(array_data)
    data = np.array(array_data, dtype=np.int32)
    actual = get_exact_cover(data)
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
    data = np.array(array_data, dtype=np.int32)
    actual = get_exact_cover(data)
    assert actual.size > 0
    assert actual.size <= rowcount
    assert all(actual < rowcount)
