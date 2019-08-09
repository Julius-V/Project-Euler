from math import sqrt, floor


# Find the period of the continued fraction of sqrt(x)
def period_cf(x):
    m = p = 0
    d = 1
    a0 = floor(sqrt(x))
    a = a0
    while True:
        m = d * a - m
        d = (x - m ** 2) // d
        a = (a0 + m) // d
        p += 1
        if a == 2 * a0:
            return p


# Finding the number of x <= k such that period_cf(x) is odd
def sum_odd_periods(k):
    return sum([period_cf(x) % 2 == 1 for x in range(1, k + 1) if sqrt(x) != round(sqrt(x))])


print(sum_odd_periods(10000))
