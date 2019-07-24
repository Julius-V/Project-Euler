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


# Producing a string of sorted digits of n
def sort_number(n):
    return ''.join(sorted(str(n)))


# Extract the arithmetic progression of 3 elements, if possible
def extract_arithmetic(ns):
    for a in range(len(ns) - 2):
        for b in range(a + 1, len(ns) - 1):
            for c in range(b + 1, len(ns)):
                if ns[b] - ns[a] == ns[c] - ns[b]:
                    return [ns[a], ns[b], ns[c]]
    return []


# Getting a list of strings formed by concatenating all the 4-tuples of interest
def prime_permutations():
    primes = sieve_sundaram(10000)
    primes = list(filter(lambda n: len(str(n)) == 4, primes))
    sorted_primes = list(map(sort_number, primes))
    candidates = [i for i in sorted_primes if sorted_primes.count(i) >= 3]
    o = []
    for candidate in candidates:
        idx = [i for i, x in enumerate(sorted_primes) if x == candidate]
        ps = extract_arithmetic([primes[i] for i in idx])
        if ps:
            o.append(''.join([str(i) for i in ps]))
    return set(o)


print(list(prime_permutations()))
