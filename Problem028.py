from math import floor


# Getting the nth spiral diagonal element using A200975
def nth_spiral_diagonal(n):
    return floor(n * (n + 2) / 4) + floor((n % 4) / 3) + 1


# Summing all the spiral diagonal elements of a dxd spiral
def sum_spiral_diagonals(d):
    return sum([nth_spiral_diagonal(i) for i in range(1, 2 * d)])


print(sum_spiral_diagonals(1001))
