from math import sqrt


# Finding the numbers of times integers 0, 1, ..., ul - 1 happen to be
# perimeters of a right triangle
def pythagorean_perimeters(ul):
    freqs = [0] * ul
    for a in range(ul):
        for b in range(ul):
            sc = sqrt(a ** 2 + b ** 2)
            c = int(sc)
            p = a + b + c
            if sc == c and p <= ul:
                freqs[p - 1] += 1
    return freqs.index(max(freqs)) + 1


print(pythagorean_perimeters(1000))
