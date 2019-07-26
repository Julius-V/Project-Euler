from math import factorial, floor


# Binomial coefficient (n, k)
def choose(n, k):
    numerator = 1
    for i in range(0, k):
        numerator *= n - i
    return numerator // factorial(k)


# Given n, find the number of k such that (n, k) > m
def choose_over_m(n, m):
    k = 0
    while k <= floor(n / 2):
        if choose(n, k) <= m:
            k += 1
        else:
            return n - 2 * k + 1
    return 0


# For n = 1, ..., u, finding the number of times (n, k) >= m
def count_large_choose(m, u):
    return sum([choose_over_m(n, m) for n in range(1, u + 1)])


print(count_large_choose(1000000, 100))
