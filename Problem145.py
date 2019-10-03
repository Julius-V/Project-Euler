# Checking if n is reversible
def is_reversible(n):
    if n % 10 == 0:
        return False
    m = n
    rev = 0
    while m > 0:
        rev = 10 * rev + m % 10
        m //= 10
    rev += n
    while rev > 0:
        if (rev % 10) % 2 == 0:
            return False
        rev //= 10
    return True


# Finding the number of reversible numbers below m
def sum_reversible(m):
    return sum([is_reversible(i) for i in range(1, m, 2)]) * 2


# There are no reversible number between 10^8 and 10^9
print(sum_reversible(10 ** 8))
