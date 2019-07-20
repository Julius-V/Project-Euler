from math import sqrt
import re


# Convert a word to a number
def word_to_num(word):
    return sum([ord(i) - 64 for i in word])


# Check whether a word is triangular
def is_triangular(word):
    n = word_to_num(word)
    return int(sqrt(1 + 8 * n)) == sqrt(1 + 8 * n)


# Count triangular words in a list
def count_triangular(ws):
    return sum([is_triangular(w) for w in ws])


with open('p042_words.txt') as f:
    words = f.read()
words = re.sub('"', '', words)
words = words.split(',')
print(count_triangular(words))
