from math import sqrt


# Finding the greatest common divisor for a, b > 0
def gcd(a, b):
    return gcd(abs(a - b), min(a, b)) if a != b else a


# Given that L is the length of the wire, finding how many values of
# L ≤ u can exactly one integer sided right angle triangle be formed
def singular_integer_tri(u):
    ns = [0] * (u + 1)
    r = 0
    lim = round(sqrt(u / 2))
    for m in range(2, lim):
        for n in range(1, m):
            if (n + m) % 2 == 1 and gcd(n, m) == 1:
                p = p0 = 2 * m * (m + n)
                while p <= u:
                    ns[p] += 1
                    if ns[p] == 1:
                        r += 1
                    if ns[p] == 2:
                        r -= 1
                    p += p0
    return r


print(singular_integer_tri(1500000))
