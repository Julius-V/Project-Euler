import re


# Replacing roman numerals r to strings of the same length as their efficient counterparts
def efficient_roman(r):
    return re.sub('IIII|VIIII|XXXX|LXXXX|CCCC|DCCCC', '--', r)


# Loading roman numerals
with open('p089_roman.txt') as f:
    numerals = f.read()


print(len(numerals) - len(efficient_roman(numerals)))
