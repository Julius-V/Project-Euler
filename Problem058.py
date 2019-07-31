from math import floor, sqrt


# Getting the nth spiral diagonal element using A200975
def nth_spiral_diagonal(n):
    return floor(n * (n + 2) / 4) + floor((n % 4) / 3) + 1


# Checking if n is a prime
def is_prime(n):
    d = 2
    while d <= floor(sqrt(n)):
        if n % d == 0:
            return False
        d += 1
    return True


# Finding the side length of the square spiral for which the ratio
# of primes along both diagonals first falls below 10%
def spiral_primes():
    n_primes = 0
    n = 1
    while True:
        n_primes += sum([is_prime(nth_spiral_diagonal(n + i)) for i in [1, 2, 3, 4]])
        n += 4
        if n_primes / n < 0.1:
            return (n - 1) // 2 + 1


print(spiral_primes())
