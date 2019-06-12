def reverse(n):
    m = 0
    while n > 0:
        m = 10 * m + n % 10
        n //= 10
    return m

def largestPalindrome():
    largest = 0
    for a in range(999, 99, -1):
        for b in range(999, 99, -1):
            if a * b > largest:
                if a * b == reverse(a * b):
                    largest = a * b
    return largest

print(largestPalindrome())