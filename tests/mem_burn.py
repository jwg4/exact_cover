import sys

import numpy as np
import exact_cover as ec

S = np.array(
    [[1, 0, 0, 1, 0], [1, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 1]], dtype=np.int32
)

if __name__ == '__main__':
    count = int(sys.argv[1])

    for i in range(count):
        print(i)
        ec.get_exact_cover(S)
