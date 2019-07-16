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


# Finding the sum of the only eleven primes that are both truncatable
# from left to right and right to left
def sum_truncatable_primes():
    primes = [2] + sieve_sundaram(1000000)
    primes = list(filter(lambda n: len(str(n)) == 1 or set(str(n)[1:]).issubset({'1', '3', '7', '9'}), primes))
    s = 0
    for p in primes[4:]:
        truncatable = True
        p = str(p)
        for i in range(1, len(p)):
            truncatable = truncatable and (int(''.join(p[i:])) in primes) and (int(''.join(p[:-i])) in primes)
            if not truncatable:
                break
        if truncatable:
            s += int(p)
    return s


print(sum_truncatable_primes())
