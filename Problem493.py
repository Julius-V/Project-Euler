

# b coloured balls, c balls of each colour.
# Finding the expected number of distinct colours in p randomly picked balls
def expected_colours(b, c, p):
    i = 1
    ps = [0, 1]
    while i < p:
        i += 1
        p_lag = ps
        ps = [0]
        for n in range(1, i + 1):
            t = 0
            k = max([0, c * n - i + 1])
            if n < i:
                t += p_lag[n] * k / (b - i + 1)
            if n > 1:
                t += p_lag[n - 1] * (b - (n - 1) * c) / (b - i + 1)
            ps.append(t)
    return sum([i * ps[i] for i in range(p + 1)])


print(expected_colours(70, 10, 20))
