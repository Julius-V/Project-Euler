from math import floor, sqrt


# Using the sieve of Sundaram to generate primes up to upper_limit
def sieve_sundaram(upper_limit):
    sieve_limit = floor((upper_limit - 2) / 2)
    nums = [True] * (sieve_limit + 1)
    nums[0] = False
    for i in range(1, floor(sieve_limit / 2)):
        for j in range(1, floor(sieve_limit / 2)):
            num = i + j + 2 * i * j
            if num <= sieve_limit:
                if nums[num]:
                    nums[num] = False
            else:
                break
    return [2 * i + 1 for i in range(sieve_limit) if nums[i]]


# Checking if n is a perfect square
def is_perfect_square(n):
    return round(sqrt(n)) == sqrt(n)


# Finding a minimal counterexample to Goldbach's conjecture
def goldbach_counterexample(k):
    primes = sieve_sundaram(k)
    n = 9
    while True:
        if n not in primes:
            for p in primes:
                if p > n:
                    return n
                if is_perfect_square((n - p) / 2):
                    break
        n += 2


print(goldbach_counterexample(10000))
