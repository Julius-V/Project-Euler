# Finding the last m digits of a ^^ b
def hyperexp(a, b, m):
    p = 1
    for e in range(b):
        p = pow(a, p, 10 ** m)
    return p


print(hyperexp(1777, 1855, 8))
