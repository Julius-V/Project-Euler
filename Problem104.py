from math import log10, sqrt


# If n is 9-digit pandigital
def is_9pandigital(n):
    n = str(n)
    return set(n) == {str(i) for i in range(1, 10)}


# Given that Fk is the first Fibonacci number for which the
# first nine digits AND the last nine digits are 1-9 pandigital, we find k
def double_pandigital_fibo():
    k = 2
    a = b = 1
    while True:
        k += 1
        a, b = b, (a + b) % (10 ** 9)
        if is_9pandigital(b):
            c = k * log10((1 + sqrt(5)) / 2) - log10(5) / 2
            if is_9pandigital(int(pow(10, c - c // 1 + 8))):
                return k


print(double_pandigital_fibo())
