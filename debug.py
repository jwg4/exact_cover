import logging

import numpy as np

from exact_cover import get_exact_cover


def run_debug():
    logging.basicConfig(level=logging.DEBUG)
    data = np.genfromtxt("tests/files/pentominos_chessboard.csv", dtype=np.int32)
    logging.info(data.shape)
    solution = get_exact_cover(data, True)
    logging.info(solution)
