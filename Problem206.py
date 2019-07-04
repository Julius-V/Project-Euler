from math import ceil, floor, sqrt


# Check if n is of the form 1_2_3_4_5_6_7_8_9_0
def magic_form(n):
    n_str = str(n)
    return [n_str[i] for i in range(0, 19, 2)] == list(map(str, list(range(1, 10)) + [0]))


# Finding the unique integer whose square is of the form 1_2_3_4_5_6_7_8_9_0
def unique_root():
    k = floor(sqrt(1020304050607080900))
    k = 1389019170 - 10
    while not magic_form(k ** 2):
        k += 1
    return k


print(unique_root())
