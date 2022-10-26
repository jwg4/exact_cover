import numpy as np

DTYPE_FOR_ARRAY = np.int32


def load_problem(filename):
    return np.genfromtxt(filename, dtype=DTYPE_FOR_ARRAY)


def save_problem(filename, array):
    np.savetxt(filename, array)
