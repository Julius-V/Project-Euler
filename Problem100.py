

# Finding the first arrangement to contain over m discs in total
# and returning the number of blue discs
def min_blue_discs(m):
    b, n = 15, 21
    while n < m:
        b, n = 3 * b + 2 * n - 2, 4 * b + 3 * n - 3
    return b


print(min_blue_discs(10 ** 12))
