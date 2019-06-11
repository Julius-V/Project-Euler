from math import sqrt

def maxPrimeFactor(n):
    p = 2
    largest = None
    while p <= sqrt(n):
        while n % p == 0:
            n /= p
            largest = p
        p += 1
    return n if n > 1 else largest

print(maxPrimeFactor(600851475143))