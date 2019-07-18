from math import floor, sqrt
import itertools


# Checking if n is a prime
def is_prime(n):
    d = 2
    while d <= floor(sqrt(n)):
        if n % d == 0:
            return False
        d += 1
    return True


# Finding the largest pandigital prime
def max_pandigital_prime():
    pandigitals = itertools.permutations('1234567', 7)
    pandigitals = map(lambda n: int(''.join(n)), pandigitals)
    pandigitals = filter(is_prime, pandigitals)
    return max(pandigitals)


print(max_pandigital_prime())
