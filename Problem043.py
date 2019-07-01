import itertools


# Checking whether n satisfied the specified divisibility property
# (without checking that d2d3d4 is even)
def substr_divisible(n):
    divisors = [2, 3, 5, 7, 11, 13, 17]
    return sum(int(str(n)[(1 + i):(4 + i)]) % divisors[i] == 0 for i in range(1, len(divisors))) == len(divisors) - 1


# Checking whether the 4th and 6th digits of n are even and divisible by 5, respectively
def d4_d6(n):
    return int(n[3]) % 2 == 0 and int(n[5]) in [0, 5]


# Finding the sum of all pandigital integers n such that substr_divisible(n) == True
def sum_substr_pandigitals():
    s = 0
    pandigitals = itertools.permutations('0123456789', 10)
    pandigitals = filter(d4_d6, pandigitals)
    for i in pandigitals:
        num = int(''.join(i))
        s += num if substr_divisible(num) else 0
    return s


print(sum_substr_pandigitals())
