# The sum d + 2d + ... + kd, where k is the largest integer such that kd <= n
def arith_prog(d, n):
    return d * (n // d) * ((n // d) + 1) // 2


# The sum of all the distinct multiples of 3 and 5 up to 1000
def sum_mult_3n5(n):
    return arith_prog(3, n) + arith_prog(5, n) - arith_prog(3 * 5, n)


print(sum_mult_3n5(1000))
