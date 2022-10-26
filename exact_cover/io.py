import numpy as np

DTYPE_FOR_CSV = np.int32


def load_problem(filename):
    return np.genfromtxt(filename, dtype=DTYPE_FOR_CSV)


def save_problem(filename, array):
    np.savetxt(filename, array)
