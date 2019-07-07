# Sum of the squares of the first n positive integers
def sum_of_squares(n):
    return n * (n + 1) * (2 * n + 1) // 6


# Square of the sum of the first n positive integers
def square_of_sum(n):
    return (n * (n + 1) / 2) ** 2


print(square_of_sum(100) - sum_of_squares(100))
