# Dictionary
dct = {0: 0, 1: len('one'), 2: len('two'), 3: len('three'), 4: len('four'), 5: len('five'),
       6: len('six'), 7: len('seven'), 8: len('eight'), 9: len('nine'), 10: len('ten'),
       11: len('eleven'), 12: len('twelve'), 13: len('thirteen'), 14: len('fourteen'),
       15: len('fifteen'), 16: len('sixteen'), 17: len('seventeen'), 18: len('eighteen'),
       19: len('nineteen'), 20: len('twenty'), 30: len('thirty'), 40: len('forty'),
       50: len('fifty'), 60: len('sixty'), 70: len('seventy'), 80: len('eighty'),
       90: len('ninety'), 100: len('hundred'), 1000: len('onethousand')}


# The number of letters when n is written out in words
def num_word_length(n):
    if n in list(range(20)) + [1000]:
        return dct[n]
    elif n >= 100:
        s = dct[100] + dct[n // 100]
        if n % 100 != 0:
            s += len('and') + num_word_length(n % 100)
        return s
    else:
        return dct[n % 10] + dct[n - n % 10]


# Number of letters used if a, a+1, ..., b were written out in words
def sum_num_word_length(a, b):
    return sum([num_word_length(i) for i in range(a, b + 1)])


print(sum_num_word_length(1, 1000))
