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
                    return int(x * y * z)


print(special_triplet(1000))
