

# Counting unique proper fractions a / b for b <= k
# The problem is equivalent to sum_{i = 2}^k phi(i),
# where phi is the Euler's totient function
def count_unique_proper_fractions(k):
    s = 0
    phi = list(range(k + 1))
    for d in range(2, k + 1):
        if phi[d] == d:
            for i in range(d, k + 1, d):
                phi[i] *= 1 - 1 / d
        s += phi[d]
    return int(s)


print(count_unique_proper_fractions(1000000))
