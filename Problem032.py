# If n is 9-digit pandigital
def is_9pandigital(n):
    return set(n) == {str(i) for i in range(1, 10)}


# Finding the sum of all products whose multiplicand/multiplier/product
# identity can be written as a 1 through 9 pandigital.
def pandigital_products():
    s = []
    a = 1
    while True:
        if a >= 1000:
            break
        b = a
        while True:
            o = str(a) + str(b) + str(a * b)
            if len(o) > 9:
                break
            elif is_9pandigital(o):
                s.append(a * b)
            b += 1
        a += 1
    return sum(set(s))


print(pandigital_products())
