# Numerator of the nth convergent of e
def nth_convergent(n):
    h = [1, 2 * 1 + 0]
    for i in range(1, n):
        a = 2 * ((i // 3) + 1) if (i - 2) % 3 == 0 else 1
        h.append(a * h[-1] + h[-2])
    return sum([int(i) for i in str(h[-1])])


print(nth_convergent(100))
