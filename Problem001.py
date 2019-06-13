def arith_prog(d, N):
    return d * (N // d) * ((N // d) + 1) / 2

def sum_mult_3n5(N):
    return arith_prog(3, N) + arith_prog(5, N) - arith_prog(3 * 5, N);

print(sum_mult_3n5(1000))
