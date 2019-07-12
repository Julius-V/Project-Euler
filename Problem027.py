from math import floor, sqrt


# Checking if n is a prime
def is_prime(n):
    d = 2
    if n < 0:
        return False
    while d <= floor(sqrt(n)):
        if n % d == 0:
            return False
        d += 1
    return True


# Defining a quadratic polynomial
def quad_poly(a, b):
    return lambda n: n ** 2 + a * n + b


# Counting the number of primes that a polynomial produces
def count_primes(poly):
    n = 0
    while is_prime(poly(n)):
        n += 1
    return n


# Finding the product of a and b such that |a| < 1000 and |b| <= 1000 and
# quad_poly(a, b) produces the most primes in a row
# Note that a and b must be odd, and b must be positive
def primest_poly():
    best = 0
    best_ab = []
    for a in range(-1000 + 1, 1000, 2):
        for b in range(1, 1000, 2):
            primes = count_primes(quad_poly(a, b))
            if primes > best:
                best = primes
                best_ab = [a, b]
    return best_ab[0] * best_ab[1]


print(primest_poly())
