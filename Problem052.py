# Transform a number into a sorted list of digits
def int_to_digits(n):
    return sorted([int(d) for d in str(n)])


# The smallest positive integer x such that ax, bx, ... contain the same digits
# where m = (a, b, ...)
def permuted_multiples(m):
    num = 1
    while True:
        lists = [int_to_digits(n * num) for n in m]
        if len(set(tuple(i) for i in lists)) <= 1:
            return num
        else:
            num += 1


print(permuted_multiples([2, 3, 4, 5, 6]))
