from math import factorial


# Sum of digits of a positive integer n
def sum_of_digits(n):
    return sum([int(i) for i in str(n)])


print(sum_of_digits(factorial(100)))
