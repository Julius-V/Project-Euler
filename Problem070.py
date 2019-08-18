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


# Is n a permutation of m?
def is_permutation(n, m):
    return sorted(str(n)) == sorted(str(m))


# Finding the value of n, 1 < n < k, for which φ(n) is a permutation of
# n and the ratio n/φ(n) produces a minimum
def totient_permutation(k):
    best = 1
    best_ratio = float('inf')
    primes = list(filter(lambda x: x > (sqrt(k) // 2), sieve_sundaram(2 * sqrt(k))))
    for i in primes:
        for j in primes:
            phi = (i - 1) * (j - 1)
            n = i * j
            ratio = n / phi
            if ratio < best_ratio and is_permutation(n, phi) and n < k:
                best = n
                best_ratio = ratio
    return best


print(totient_permutation(10 ** 7))
