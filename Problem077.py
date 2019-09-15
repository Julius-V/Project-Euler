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
    return [2] + [2 * i + 1 for i in range(sieve_limit) if nums[i]]


# Counting the number of different ways 'amount' can be made using elems
def partitions(amount, elems):
    s = 0
    if len(elems) == 0:
        return 0
    if amount % elems[0] == 0:
        s += 1
    for t in range(amount // elems[0] + (amount % elems[0] != 0)):
        s += partitions(amount - t * elems[0], elems[1:])
    return s


# Finding the first value which can be written as the sum of primes
# in over five thousand different ways
def prime_partitions():
    primes = sieve_sundaram(100000)
    n = 2
    while True:
        if partitions(n, [p for p in primes if p <= n]) > 5000:
            return n
        n += 1


print(prime_partitions())
