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


# Check for single-digit number of only consisting of [1, 3, 7, 9]
def circular_check(p):
    good_int = {1, 3, 7, 9}
    p = str(p)
    p_digits = set(map(int, p))
    return len(p) == 1 or p_digits.issubset(good_int)


# Get all rotations of p
def get_rotations(p):
    for i in range(len(p)):
        yield int(''.join(p[i::] + p[0:i]))


# Counting all circular primes
def circular_primes():
    primes = [2] + list(filter(circular_check, sieve_sundaram(1000000)))
    return sum([False not in [rot in primes for rot in get_rotations(str(p))] for p in primes])


print(circular_primes())
