import numpy as np


# Finding the minimal path sum going just down or right
def path_sum(m):
    # Square matrix size
    n = np.size(m, 0)
    # First row/column
    m[0, 1:] += np.cumsum(m[0, :-1])
    m[1:, 0] += np.cumsum(m[:-1, 0])
    # The rest
    for r in range(1, n):
        # Diagonal element
        m[r, r] += min(m[r - 1, r], m[r, r - 1])
        # Off-diagonal elements
        for i in range(r + 1, n):
            m[r, i] += min(m[r - 1, i], m[r, i - 1])
            m[i, r] += min(m[i - 1, r], m[i, r - 1])
    return m[n - 1, n - 1]


# Loading data
data = np.loadtxt("p081_matrix.txt", dtype='int', delimiter=',')
print(path_sum(data))
