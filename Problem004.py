# Reversing the digits of a number n
def reverse(n):
    m = 0
    while n > 0:
        m = 10 * m + n % 10
        n //= 10
    return m


# Finding the largest palindrome that is a product of two n-digit numbers
def largest_palindrome(n):
    largest = 0
    for a in range(10 ** n - 1, 10 ** (n - 1) - 1, -1):
        for b in range(10 ** n - 1, 10 ** (n - 1) - 1, -1):
            if a * b > largest:
                if a * b == reverse(a * b):
                    largest = a * b
    return largest


print(largest_palindrome(3))
