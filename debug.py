import numpy as np

from exact_cover import get_exact_cover


def run_debug():
    data = np.genfromtxt("tests/files/part_reduced.csv", dtype=np.int32)
    get_exact_cover(data, True)
