from math import floor


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


# Get the number of distinct prime divisors of n given primes_list
def distinct_prime_divisors(n, primes_list, lim):
    i = s = 0
    init = n
    while primes_list[i] <= n and s <= lim:
        if n % primes_list[i] == 0:
            s += 1
            while n % primes_list[i] == 0:
                n //= primes_list[i]
        if primes_list[i] ** 2 > init and n > 1:
            return s + 1 == lim
        i += 1
    return s == lim


# Find the first k consecutive numbers that have k distinct prime factors
def k_consecutive_k_factors(k):
    primes = [2] + sieve_sundaram(200000)
    n = k
    divisors = [distinct_prime_divisors(i, primes, k) for i in range(n - k + 1, n + 1)]
    while True:
        if not divisors[k - 1]:
            n += k
            divisors = [distinct_prime_divisors(i, primes, k) for i in range(n - k + 1, n + 1)]
        elif all(divisors):
            return n - k + 1
        else:
            n += 1
            divisors = divisors[1:] + [distinct_prime_divisors(n, primes, k)]


print(k_consecutive_k_factors(4))
