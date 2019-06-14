# Even Fibonacci sequence terms up to n
def even_fibo(n):
    a, b = 1, 2
    while a < n:
        yield a if a % 2 == 0 else 0
        a, b = b, a + b


print(sum(even_fibo(4000000)))
