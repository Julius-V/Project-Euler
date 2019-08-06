from math import ceil


# Counting the number of n-digit positive integers which also are an nth power
def n_digit_n_power():
    s = 0
    p = 1
    while True:
        x = ceil(10 ** ((p - 1) / p))
        if x < 10:
            s += 10 - x
            p += 1
        else:
            break
    return s


print(n_digit_n_power())
