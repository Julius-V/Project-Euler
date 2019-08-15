import itertools


# Is g a magic 5-gon potentially giving the maximum 16-digit string?
def is_magic_5gon(g):
    return min([g[i] for i in [0, 3, 5, 7, 9]]) == g[0] and \
           10 not in [g[i] for i in [1, 2, 4, 6, 8]] and \
           g[0] + g[1] == g[3] + g[4] and g[3] + g[2] == g[5] + g[6] and \
           g[5] + g[4] == g[7] + g[8] and g[7] + g[6] == g[9] + g[1] and \
           g[9] + g[8] == g[0] + g[2]


# Transform a 5-gon to a string
def gon_to_int(g):
    return int(''.join([str(g[i]) for i in [0, 1, 2, 3, 2, 4, 5, 4, 6, 7, 6, 8, 9, 8, 1]]))


# Finding the maximum 16-digit string for a "magic" 5-gon ring
def max_string_magic_5gon():
    return max(map(gon_to_int, filter(is_magic_5gon, itertools.permutations(range(11), 10))))


print(max_string_magic_5gon())
