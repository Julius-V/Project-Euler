

# The total number of rectangles in a mxn grid
# Sum (m-k+1)(n-l-1) over k=1,...,m and l=1,...n to get the following
def sum_grid_rectangles(m, n):
    return m * n * (n + 1) * (m + 1) / 4


# Finding the area of the grid with the number of rectangles closest to 'target'
def nearest_grid(target):
    best_score = 0
    best_area = 0
    for m in range(100):
        for n in range(100):
            if abs(sum_grid_rectangles(m, n) - target) < abs(best_score - target):
                best_score = sum_grid_rectangles(m, n)
                best_area = m * n
    return best_area


print(nearest_grid(2000000))
