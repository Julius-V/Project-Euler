

# Finding the value of d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000,
# if dn represents the nth digit of the fractional part of the Champernowne's constant
def champernowne_cons():
    prod = k = t = n = 1
    while k < 7:
        n += 1
        if (t < 10 ** k) and (t + len(str(n))) >= 10 ** k:
            prod *= int(str(n)[10 ** k - t - 1])
            k += 1
        t += len(str(n))
    return prod


print(champernowne_cons())
