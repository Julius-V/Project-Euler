from math import factorial


# Starting from n, whether the chain ends in 1 or 89
def square_digit_chain(n):
    if n in [1, 89]:
        return n
    else:
        return square_digit_chain(sum([int(k) ** 2 for k in str(n)]))


# The number of starting numbers below ten million that arrive at 89
def square_digit_chains():
    s = 0
    for ones in range(0, 7 + 1):
        for twos in range(0, 7 + 1 - ones):
            for threes in range(0, 7 + 1 - ones - twos):
                for fours in range(0, 7 + 1 - ones - twos - threes):
                    for fives in range(0, 7 + 1 - ones - twos - threes - fours):
                        for sixes in range(0, 7 + 1 - ones - twos - threes - fours - fives):
                            for sevens in range(0, 7 + 1 - ones - twos - threes - fours - fives - sixes):
                                for eights in range(0, 7 + 1 - ones - twos - threes - fours - fives - sixes - sevens):
                                    for nines in range(0, 7 + 1 - ones - twos - threes - fours - fives - sixes - sevens - eights):
                                        for zeroes in range(0, 7 + 1 - ones - twos - threes - fours - fives - sixes - sevens - eights - nines):
                                            if ones + twos + threes + fours + fives + \
                                                    sixes + sevens + eights + nines + zeroes == 7 and zeroes < 7:
                                                n = ones + twos * 4 + threes * 9 + fours * 16 + fives * 25 + \
                                                    sixes * 36 + sevens * 49 + eights * 64 + nines * 81
                                                if square_digit_chain(n) == 89:
                                                    s += factorial(7) // (factorial(ones) * factorial(twos) *
                                                                          factorial(threes) * factorial(fours) *
                                                                          factorial(fives) * factorial(sixes) *
                                                                          factorial(sevens) * factorial(eights) *
                                                                          factorial(nines) * factorial(zeroes))
    return s


print(square_digit_chains())
