from scipy.special import comb


# The number of paths from the top left corner to the
# bottom right corner on an n x n lattice
def lattice_paths(n):
    return comb(2 * n, n, exact=True)


print(lattice_paths(20))
