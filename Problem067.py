# nth triangular number
def nth_trianglar(n):
    return n * (n + 1) // 2


# Extracting the nth element of the rth row of a given triangle
# filled with (width-1)-digit number
def triangle_elem(triangle, width, r, n):
    n = nth_trianglar(r - 1) * width + (n - 1) * width
    return int(triangle[n:(n + width - 1)])


# Finding the maximal path sum by iterating from top to bottom
def max_path_sum(triangle, width, rows):
    v = [triangle_elem(triangle, width, 1, 1)]
    for r in range(2, rows + 1):
        v.append(triangle_elem(triangle, width, r, r) + v[r - 2])
        for e in range(r - 1, 1, -1):
            v[e - 1] = triangle_elem(triangle, width, r, e) + max(v[e - 1], v[e - 2])
        v[0] = triangle_elem(triangle, width, r, 1) + v[0]
    return max(v)


tri = open('p067_triangle.txt', 'r').read()

print(max_path_sum(tri, 3, 100))
