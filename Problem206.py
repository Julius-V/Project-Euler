from math import floor, sqrt


# n^2 = 0 mod 10 if and only if n ends with a zero
#
# In that case 1_2_3_4_5_6_7_8_9_0 = 1_2_3_4_5_6_7_8_900 and (n / 10)^2 = 1_2_3_4_5_6_7_8_9
# It follows that (n / 10) = 3 or 7 mod 10

# Finding the unique integer whose square is of the form 1_2_3_4_5_6_7_8_9_0
def unique_root():
    k = floor(sqrt(10203040506070809)) // 10 * 10 + 3
    aux = [str(i) for i in range(1, 10)]
    while True:
        idx = True
        n = str(k ** 2)
        for i in range(0, 17, 2):
            idx = n[i] == aux[i // 2]
            if not idx:
                break
        if idx:
            return k
        k += 4
        n = str(k ** 2)
        for i in range(0, 17, 2):
            idx = n[i] == aux[i // 2]
            if not idx:
                break
        if idx:
            return k
        k += 6


print(unique_root())
