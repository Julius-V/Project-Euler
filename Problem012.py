from math import sqrt, ceil


# The number of divisors of n
def divisors(n):
    d = 0
    # Adding two for each divisor below sqrt(n)
    for i in range(1, ceil(sqrt(n))):
        if n % i == 0:
            d += 2
    # And one if a perfect square
    if sqrt(n) == round(sqrt(n)):
        d += 1
    return d


# The smallest triangular number >= k
def next_triangular(k):
    n = ceil(sqrt(1 + 8 * k) / 2 - 1 / 2)
    return n * (n + 1) / 2


# The smallest triangular number with 500 or more divisors
def min_divisible_tri():
    # Starting point = num + 1 is the smallest integer with 500 divisors
    num = 2 ** 4 * 3 ** 4 * 5 ** 4 * 7 * 11 - 1
    d = 0
    while d <= 500:
        num = next_triangular(num + 1)
        d = divisors(num)
    return num


print(min_divisible_tri())
