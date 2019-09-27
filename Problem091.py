# Finding the greatest common divisor for a, b > 0
def gcd(a, b):
    return gcd(abs(a - b), min(a, b)) if a != b else a


# Finding how many right triangles can be former given that
# 0 ≤ x1, y1, x2, y2 ≤ m
def num_tri(m):
    o = 3 * m ** 2
    for x in range(1, m + 1):
        for y in range(1, m + 1):
            n = gcd(x, y)
            o += min(y * n // x, (m - x) * n // y) * 2
    return o


print(num_tri(50))
