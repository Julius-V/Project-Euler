# A problem analogous to Problem 31 but now needs dynamic programming


# Counting partitions of n using 1, ..., k
def partitions(n, k):
    ns = [1] + [0] * n
    for i in range(1, k + 1):
        for j in range(i, len(ns)):
            ns[j] += ns[j - i]
    return ns[-1]


print(partitions(100, 99))
