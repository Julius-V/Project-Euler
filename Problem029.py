# The number of distinct numbers a^b where ll <= a, b <= ul
def num_distinct_powers(ll, ul):
    out = []
    for a in range(ll, ul + 1):
        for b in range(ll, ul + 1):
            out.append(a ** b)
    return len(set(out))


print(num_distinct_powers(2, 100))
