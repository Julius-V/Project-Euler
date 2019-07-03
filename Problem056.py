# Sum of digits of integer n
def sum_of_digits(n):
    return sum([int(i) for i in str(n)])


# Finding the largest digit sum of a^b, where a, b < c
def largest_digit_sum(c):
    largest = 0
    for a in range(c):
        for b in range(c):
            new_sum = sum_of_digits(a ** b)
            if new_sum > largest:
                largest = new_sum
    return largest


print(largest_digit_sum(100))
