# Returning the index of the first k-digit Fibonacci number
def first_fibo_n_digits(k):
    a, b = 0, 1
    i = 1
    while len(str(b)) != k:
        a, b = b, a + b
        i += 1
    return i


print(first_fibo_n_digits(1000))
