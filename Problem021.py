from math import sqrt, ceil


# The sum of proper divisors of n
def sum_pdivisors(n):
    s = 1
    for i in range(2, ceil(sqrt(n))):
        if n % i == 0:
            s += i + n // i
    if sqrt(n) == round(sqrt(n)):
        s += round(sqrt(n))
    return s


# Sum all the pairs of amicable numbers below m
def sum_amicable(m):
    s = 0
    for i in range(2, m):
        a = sum_pdivisors(i)
        if (a > i) & (sum_pdivisors(a) == i):
            print(i, a)
            s += i + a
    return s

print(sum_amicable(10000))
