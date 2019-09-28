from math import floor, ceil, sqrt
import bisect


# Searching in a sorted list
def index(a, x):
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    return -1


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
    return [2] + [2 * i + 1 for i in range(sieve_limit) if nums[i]]


# Divisors of n up to sqrt(n)
def divisors(n):
    for i in range(1, ceil(sqrt(n)) + 1):
        if (n % i) == 0:
            yield i


# Is n such that that for every divisor d of n, d + n / d is prime?
def is_prime_gen_int(n, primes):
    for d in divisors(n):
        r = d + n // d
        if index(primes, r) == -1:
            return 0
    return n


# Finding the sum of all positive integers n not exceeding 100 000 000
# such that for every divisor d of n, d + n / d is prime
def sum_prime_gen_ints(primes):
    return sum([is_prime_gen_int(p - 1, primes) for p in primes])


print(sum_prime_gen_ints(sieve_sundaram(100000000)))
