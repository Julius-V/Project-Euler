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


# Find a rolling sum of x with window h and resulting terms below g, except for the last element
def roll_sum(x, h, g):
    o = [sum(x[0:h])]
    p = 1
    while o[len(o) - 1] < g:
        o.append(sum(x[p:(p + h)]))
        p += 1
    return o


# Finding which prime, below k, can be written as the sum of the most consecutive primes
def as_sum_consecutive_primes(k):
    primes = [2] + sieve_sundaram(k)
    best = 953
    for h in range(21, k, 2):
        rs = roll_sum(primes, h, k)
        if rs[0] > k:
            break
        intrs = set(primes).intersection(rs)
        if len(intrs) > 0:
            best = intrs
    return best


print(as_sum_consecutive_primes(1000000))
