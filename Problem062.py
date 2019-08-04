import itertools
import operator


# Finding the most common element in a list
# (https://stackoverflow.com/a/1520716/1320535)
def most_common(lst):
    sl = sorted((x, i) for i, x in enumerate(lst))
    groups = itertools.groupby(sl, key=operator.itemgetter(0))

    def _auxfun(g):
        item, iterable = g
        count = 0
        min_index = len(lst)
        for _, where in iterable:
            count += 1
            min_index = min(min_index, where)
        return count, -min_index

    return max(groups, key=_auxfun)[0]


# Producing a string of sorted digits of n
def sort_number(n):
    return ''.join(sorted(str(n)))


# Finding the smallest cube for which exactly p permutations of its digits are cube
def cube_permutations(p):
    for digits in [2, 3]:
        cubes = [i ** 3 for i in range(10 ** digits, 10 ** (digits + 1))]
        sorted_cubes = list(map(sort_number, cubes))
        mc = most_common(sorted_cubes)
        if sorted_cubes.count(mc) == p:
            return cubes[sorted_cubes.index(most_common(sorted_cubes))]


print(cube_permutations(5))
