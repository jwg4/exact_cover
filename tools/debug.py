import logging
import sys

import numpy as np

from ValgrindCI.parse import ValgrindData

from exact_cover import get_exact_cover


def run_debug():
    logging.basicConfig(level=logging.DEBUG)
    data = np.genfromtxt("tests/files/pentominos_chessboard.csv", dtype=np.int32)
    logging.info(data.shape)
    solution = get_exact_cover(data, True)
    logging.info(solution)


def parse_valgrind_results():
    data = ValgrindData()
    data.parse("valgrind_results.xml")
    # Output the number of errors for leaks definitely lost.
    leak_count = data.filter_error_kind("Leak_DefinitelyLost").get_num_errors()
    print("Definite leaks: ", leak_count)
    # One leak seems like a mis-diagnosis - caused by
    # returning a C array wrapped as a Python obj?
    if leak_count > 1:
        sys.exit(1)
    else:
        sys.exit(0)
