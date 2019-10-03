# Get the sign of n
def sign(n):
    if n < 0:
        return -1
    elif n > 0:
        return 1
    else:
        return 0


# Check whether n is bouncy
def is_bouncy(n):
    n = str(n)
    signs = [sign(int(n[i]) - int(n[i - 1])) for i in range(1, len(n))]
    return max(signs) == 1 and min(signs) == -1


# Finding the least number for which the proportion of bouncy numbers is exactly thr * 100%
def thr_bouncy(thr):
    bouncy = 0
    n = 100
    while bouncy / n != thr:
        n += 1
        bouncy += is_bouncy(n)
    return n


print(thr_bouncy(99 / 100))
