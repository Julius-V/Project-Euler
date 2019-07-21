from math import sqrt


# Check if n is a perfect square
def is_square(n):
    return round(sqrt(n)) == sqrt(n)


# Check if n is pentagonal
def is_pentagonal(n):
    return is_square(24 * n + 1) and sqrt(24 * n + 1) % 6 == 5


# nth pentagonal number
def pentagonal(n):
    return n * (3 * n - 1) // 2


# Finding minimal |P_i - P_j| such that the sum and the difference of
# pentagonal P_i and P_j are pentagonal
def min_pentagonal(k):
    d = pentagonal(k) * 2
    pentagonals = [pentagonal(1)]
    for n in range(2, k):
        p = pentagonal(n)
        for i in range(len(pentagonals)):
            if is_pentagonal(p - pentagonals[i]) and is_pentagonal(p + pentagonals[i]):
                d = min(d, p - pentagonals[i])
        pentagonals.append(p)
    return d


print(min_pentagonal(2500))
