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


tri = '\
75 \
95 64 \
17 47 82 \
18 35 87 10 \
20 04 82 47 65 \
19 01 23 75 03 34 \
88 02 77 73 07 63 67 \
99 65 04 28 06 16 70 92 \
41 41 26 56 83 40 80 70 33 \
41 48 72 33 47 32 37 16 94 29 \
53 71 44 65 25 43 91 52 97 51 14 \
70 11 33 28 77 73 17 78 39 68 17 57 \
91 71 52 38 17 14 91 43 58 50 27 29 48 \
63 66 04 68 89 53 67 30 73 16 69 87 40 31 \
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23 '

print(max_path_sum(tri, 3, 15))
