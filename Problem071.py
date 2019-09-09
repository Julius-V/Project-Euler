from math import floor, ceil


# Find the largest fraction a / b <= j, with some given bound m < a / b, where b <= k
def largest_fraction(j, m, k):
    best_a = m
    best_b = 1
    for d in range(1, k + 1):
        for n in range(floor(best_a / best_b * d), ceil(j * d)):
            if n / d > best_a / best_b and n / d < j:
                best_a = n
                best_b = d
    return [best_a, best_b]


print(largest_fraction(3 / 7, 0.42857, 1000000))
# It can be further checked that gcd(428570, 999997) = 1
