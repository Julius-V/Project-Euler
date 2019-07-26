from math import floor
import itertools
import operator


# Finding the most common element in a list
# (https://stackoverflow.com/a/1520716/1320535)
def most_common(lst):
    sl = sorted((x, i) for i, x in enumerate(lst))
    groups = itertools.groupby(sl, key=operator.itemgetter(0))

    def _auxfun(g):
        item, iterable = g
        count = 0
        min_index = len(lst)
        for _, where in iterable:
            count += 1
            min_index = min(min_index, where)
        return count, -min_index

    return max(groups, key=_auxfun)[0]


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


# Replace digits of n indexed by d with -
def replace_digits(n, d):
    n = list(str(n))
    if len(n) >= (max(d) + 1) and len(set([n[i] for i in d])) == 1:
        for i in range(len(n)):
            if i in d:
                n[i] = '-'
    return ''.join(n)


# Finding the smallest prime which, by replacing part of the number
# (not necessarily adjacent digits) with the same digit, is part of a k prime value family
def prime_family(k, m):
    primes = sieve_sundaram(10 ** m)
    for digits in [1, 2, 3]:
        combs = itertools.combinations(list(range(0, m - 1)), digits)
        for comb in combs:
            primes_tmp = list(map(lambda n: replace_digits(n, comb), primes))
            mc = most_common(primes_tmp)
            if primes_tmp.count(mc) == k:
                return primes[primes_tmp.index(mc)]


print(prime_family(8, 6))
