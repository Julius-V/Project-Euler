from math import sqrt


# Using Dickson's (1920) method to generate Pythagorean triples
# and returning that triplet (x,y,z) that satisfies x+y+z=d
def special_triplet(d):
    for s in range(1, d - 1):
        for t in range(1, d - s):
            r = sqrt(2 * s * t)
            if r == round(r):
                x = r + s
                y = r + t
                z = r + s + t
                if x + y + z == d:
                    yield 1


def most_common_perimeter():
    freqs = [sum(special_triplet(d)) for d in range(2, 1001)]
    return freqs.index(max(freqs)) + 2


print(most_common_perimeter())
