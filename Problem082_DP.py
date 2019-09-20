import numpy as np


# Finding the minimal path sum going just up, down, or right
def min_path_sum(m):
    n = np.size(m, 0)
    o = m[:, n - 1]
    for col in range(n - 2, -1, -1):
        o[0] += m[0, col]
        for row in range(1, n):
            o[row] = min(m[row, col] + o[row - 1], m[row, col] + o[row])
        for row in range(n - 2, 1, -1):
            o[row] = min(m[row, col] + o[row + 1], o[row])
    return min(o)


# Loading data
data = np.loadtxt('p082_matrix.txt', dtype='int', delimiter=',')
print(min_path_sum(data))
