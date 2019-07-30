

# Counting sqrt(2) convergents up to k, counting
# the number of times a numerator with more digits than denominator
def count_convergents(m):
    h = [1, 2 * 1 + 1]
    k = [1, 2 * 1 + 0]
    s = n = 0
    while n < m:
        h.append(2 * h[-1] + h[-2])
        k.append(2 * k[-1] + k[-2])
        s += len(str(h[-1])) > len(str(k[-1]))
        n += 1
    return s


print(count_convergents(1000))
