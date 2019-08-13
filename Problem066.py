from math import sqrt, floor


# Is (x,y) a solution to x^2 - D y^2 = 1?
def is_solution(x, y, D):
    return x ** 2 - D * y ** 2 == 1


# Find the fundamental solution to Pell's equation x^2 - D y^2 = 1
def fundamental_solution(D):
    a0 = floor(sqrt(D))
    h = a0
    k = d = h_lag = 1
    k_lag = m = 0
    if is_solution(h, k, D):
        return h
    a = a0
    while True:
        m = d * a - m
        d = (D - m ** 2) // d
        a = (a0 + m) // d
        h, h_lag = a * h + h_lag, h
        k, k_lag = a * k + k_lag, k
        if is_solution(h, k, D):
            return h


# Finding the value of D ≤ b in minimal solutions of x for which
# the largest value of x is obtained
def find_minimal_D(b):
    Ds = range(b + 1)
    xs = [fundamental_solution(D) if sqrt(D) != floor(sqrt(D)) else 0 for D in Ds]
    return Ds[xs.index(max(xs))]


print(find_minimal_D(1000))
