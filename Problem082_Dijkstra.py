import numpy as np


# Finding the minimal path sum going just up, down, or right
def path_sum(m):
    n = np.size(m, 0)
    last = 1 + (n - 2) * n
    for source in range(0, n):
        dist = np.array([float('inf')] * (1 + last))
        dist[0] = 0
        q = list(range(len(dist)))

        while len(q) > 0:
            v = list(set(q).intersection(np.where(dist == min([dist[j] for j in q]))[0]))[0]
            q.remove(v)

            if v == 0:
                neighbours = [source + 1]
            elif v == last:
                neighbours = []
            elif (v - 1) % n == 0:
                neighbours = [v + 1, min(v + n, last)]
            elif v % n == 0:
                neighbours = [v - 1, min(v + n, last)]
            else:
                neighbours = [v - 1, v + 1, min(v + n, last)]

            for u in neighbours:
                if u == last:
                    alt = dist[v] + m[(v - 1) % n, n - 1]
                else:
                    alt = dist[v] + m[(u - 1) % n, 1 + (u - 1) // n]
                if alt < dist[u]:
                    dist[u] = alt
        yield int(dist[-1] + m[source, 0])


# Loading data
data = np.loadtxt('p082_matrix.txt', dtype='int', delimiter=',')
print(min(path_sum(data)))
