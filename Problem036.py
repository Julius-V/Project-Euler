# Whether n is a palindrome in base 10
def is_palindrome_base10(n):
    return str(n) == str(n)[::-1]


# Whether n is a palindrome in base 2
def is_palindrome_base2(n):
    return str(bin(n))[2:] == str(bin(n))[2:][::-1]


# Counting palindromes from a and below b
def count_palindromes(a, b):
    return sum([i if is_palindrome_base2(i) and is_palindrome_base10(i) else 0 for i in range(a, b)])


print(count_palindromes(0, 1000000))
