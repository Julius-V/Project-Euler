from math import floor, ceil


# Counting fractions c < a / b < f for b <= k
def count_fractions_in_range(c, f, k):
    o = []
    for d in range(1, k + 1):
        for n in range(floor(c * d), ceil(f * d)):
            if c < n / d < f:
                o.append(n / d)
    return len(set(o))


print(count_fractions_in_range(1 / 3, 1 / 2, 12000))
