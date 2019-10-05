# Probability of n d-sided dices to give a total of s
def prob(n, d, s):
    if s <= 0:
        return 0
    elif n == 1 and s <= d:
        return 1 / d
    elif n > 1:
        o = 0
        for r in range(1, d + 1):
            o += prob(n - 1, d, s - r) * 1 / d
        return o
    else:
        return 0


# What is the probability that Pyramidal Pete beats Cubic Colin?
def a_beat_b(n_1, n_2, d_1, d_2):
    p = 0
    for i in range(n_1, n_1 * d_1 + 1):
        p_aux = 0
        for j in range(n_2, i):
            p_aux += prob(n_2, d_2, j)
        p += prob(n_1, d_1, i) * p_aux
    return p


print(a_beat_b(9, 6, 4, 6))
