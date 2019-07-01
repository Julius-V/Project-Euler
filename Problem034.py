from math import factorial


# Sum of digit factorials of a positive integer n
def sum_of_fact_digits(n):
    return sum([factorial(int(i)) for i in str(n)])


# Counting the sum of all such 2<n<k that n == sum_of_fact_digits(n)
def sum_curious(k):
    return sum([n if n == sum_of_fact_digits(n) else 0 for n in range(3, k)])


print(sum_curious(100000))
