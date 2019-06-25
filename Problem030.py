# Find the sum of the fifth powers of the digits of n
def is_sum_of_digit_powers(n):
    return n == sum([int(i) ** 5 for i in str(n)])


# Find the sum of all the integers > 1 that is_sum_of_digit_powers
def count_ints():
    return sum([i if is_sum_of_digit_powers(i) else 0 for i in range(2, 5 * 10 ** 6)])


print(count_ints())
