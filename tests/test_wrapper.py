import numpy as np

from exact_cover.wrapper import solutions_array_to_set


def test_solutions_array_to_set():
    input_array = np.zeros((3, 5))
    input_array[0, 0] = 7
    input_array[1, 0] = input_array[2, 0] = 8
    input_array[1, 1] = 9

    actual = solutions_array_to_set(input_array)
    expected = {(7, ), (8, ), (8, 9)}
    assert actual == expected


def test_solutions_array_to_set_wide():
    input_array = np.zeros((3, 1000))
    input_array[0, 0] = 7
    input_array[1, 0] = input_array[2, 0] = 8

    actual = solutions_array_to_set(input_array)
    expected = {(7, ), (8, )}
    assert actual == expected
