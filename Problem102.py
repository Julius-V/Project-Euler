# Checking if origin belongs to a triangle
def is_origin_in(tri):
    tri = list(map(int, tri.split(',')))
    # Redefining the origin as -A
    o = [-i for i in tri[0:2]]
    # Shifting the origin to point A
    tri = list(map(lambda a, b: a - b, tri[2:], tri[0:2] * 2))
    p_b = tri[0:2]
    p_c = tri[2:4]
    d = p_b[0] * p_c[1] - p_c[0] * p_b[1]
    # Finding barycentric weights
    w_a = (o[0] * (p_b[1] - p_c[1]) + o[1] * (p_c[0] - p_b[0])) / d + 1
    w_b = (o[0] * p_c[1] - o[1] * p_c[0]) / d
    w_c = (o[1] * p_b[0] - o[0] * p_b[1]) / d
    return max(w_a, w_b, w_c) <= 1 and min(w_a, w_b, w_c) >= 0


# Counting the number of triangles that contain (0, 0)
def sum_origin_triangles(tris):
    return sum([is_origin_in(tri) for tri in tris])


with open('p102_triangles.txt') as f:
    triangles = f.read()
triangles = triangles.split('\n')
triangles.pop(len(triangles) - 1)
print(sum_origin_triangles(triangles))
