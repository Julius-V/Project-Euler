import numpy as np


# Finding the minimal path sum going to all four directions
def path_sum(m):
    n = np.size(m, 0)
    last = n ** 2 - 1
    dist = np.array([float('inf')] * (1 + last))
    dist[0] = 0
    q = list(range(len(dist)))

    while len(q) > 0:
        v = list(set(q).intersection(np.where(dist == min([dist[j] for j in q]))[0]))[0]
        q.remove(v)

        if v == 0:
            neighbours = [1, v + n]
        elif v == last:
            neighbours = []
        elif v == (n - 1):
            neighbours = [v - 1, v + n]
        elif v < n:
            neighbours = [v - 1, v + 1, v + n]
        elif v == (last - n + 1):
            neighbours = [v - n, v + 1]
        elif v > (last - n):
            neighbours = [v - n, v - 1, v + 1]
        elif v % n == 0:
            neighbours = [v - n, v + 1, v + n]
        elif (v + 1) % n == 0:
            neighbours = [v - n, v - 1, v + n]
        else:
            neighbours = [v - 1, v + 1, v + n, v - n]

        for u in neighbours:
            alt = dist[v] + m[u % n, u // n]
            if alt < dist[u]:
                dist[u] = alt
    yield int(dist[-1] + m[0, 0])


# Loading data
data = np.loadtxt('p083_matrix.txt', dtype='int', delimiter=',')
print(min(path_sum(data)))
