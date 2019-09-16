# nth pentagonal number
def nth_pentagonal(n):
    return n * (3 * n - 1) // 2


# nth generalized pentagonal number
def nth_gen_pentagonal(n):
    m = (n + 1) // 2
    if n % 2 == 0:
        m *= -1
    return nth_pentagonal(m)


# Finding the first n such that P(n) is divisible by r
def p_div(r):
    ps = [1]
    i = 1
    while True:
        k = 1
        p = 0
        while nth_gen_pentagonal(k) <= len(ps):
            sgn = 1 if ((k + 1) // 2) % 2 == 1 else -1
            p = (p + sgn * ps[-(nth_gen_pentagonal(k))]) % r
            k += 1
        ps.append(p)
        if p == 0:
            return i
        i += 1


print(p_div(1000000))
