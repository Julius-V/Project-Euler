import re


# Alphabetical value of
def alphabetical_value(word):
    return sum([ord(word[l]) - 64 for l in range(len(word))])


# Summing word scores (alphabetical value * place in the list)
def sum_word_scores(words):
    return sum([(i + 1) * alphabetical_value(words[i]) for i in range(len(words))])


# Loading names
with open('p022_names.txt') as f:
    names = f.read()
# Removing quotation marks
names = re.sub('"', "", names)
# Splitting into a list
names = names.split(",")
# Sorting
names = sorted(names)

print(sum_word_scores(names))
