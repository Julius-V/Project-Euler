# nth triangular number
def triangular(n):
    return n * (n + 1) // 2


# nth pentagonal number
def pentagonal(n):
    return n * (3 * n - 1) // 2


# nth hexagonal number
def hexagonal(n):
    return n * (2 * n - 1)


# Finding the next triangular number after 40755 that is
# also pentagonal and hexagonal
def tri_pen_hexag():
    n_tri = 286
    tri = triangular(n_tri)
    n_pen = 166
    pen = pentagonal(n_pen)
    n_hexag = 143
    hexag = hexagonal(n_hexag)
    while tri != pen or pen != hexag:
        smallest = min([tri, pen, hexag])
        if smallest == tri:
            n_tri += 1
            tri = triangular(n_tri)
        elif smallest == pen:
            n_pen += 1
            pen = pentagonal(n_pen)
        else:
            n_hexag += 1
            hexag = hexagonal(n_hexag)
    return tri


print(tri_pen_hexag())
