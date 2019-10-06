# Finding r_max(a)
def r_max(a):
    return 2 * a * ((a - 1) // 2)


# Finding r_max(l) + ... r_max(u)
def sum_r_max(l, u):
    return sum([r_max(a) for a in range(l, u + 1)])


print(sum_r_max(3, 1000))
