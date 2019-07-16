# If n is 9-digit pandigital
def is_9pandigital(n):
    return set(n) == {str(i) for i in range(1, 10)}


# Finding the largest 1 to 9 pandigital 9-digit number that can be
# formed as the concatenated product of an integer with (1, 2, ..., n)
def max_pandigital_multiple():
    best = 918273645
    for k in range(1, 10000 + 1):
        prod = str(k)
        for l in range(2, 10):
            prod = prod + str(k * l)
            if len(prod) == 9:
                if is_9pandigital(prod):
                    best = max(best, int(''.join(prod)))
            elif len(prod) > 9:
                break
    return best


print(max_pandigital_multiple())
