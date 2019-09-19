from math import sqrt


# Sum of first m decimal digits of the square root of n
def sum_of_decimal_digits(n, m):
    return sum([int(i) for i in str(square_root(n, m))])


# The first m decimal digits of the square root of n
def square_root(n, m):
    a = 5 * n
    b = 5
    while b < 10 ** (m + 1):
        if a >= b:
            a -= b
            b += 10
        else:
            a *= 100
            b = (b // 10) * 100 + 5
    return b // 100


# The total of the digital sums of the first m digits
# for all the irrational square roots of n = 1, 2, ..., k
def sum_root_digits(k, m):
    return sum([sum_of_decimal_digits(i, m) if round(sqrt(i)) != sqrt(i) else 0 for i in range(1, k + 1)])


print(sum_root_digits(100, 100))
