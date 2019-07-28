# Reverse the digits of n
def reverse(n):
    return int(str(n)[::-1])


# Is n a palindrome?
def is_palindrome(n):
    return n == reverse(n)


# Is n a Lychrel number?
def is_lychrel(n):
    k = 1
    while k <= 50 and not is_palindrome(n + reverse(n)):
        n += reverse(n)
        k += 1
    return not is_palindrome(n + reverse(n))


# How many Lychrel number are there below m?
def count_lychrel(m):
    return sum([is_lychrel(n) for n in range(1, m)])


print(count_lychrel(10000))
