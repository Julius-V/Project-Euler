def arithmeticProgress(d, N):
    return d * (N // d) * ((N // d) + 1) / 2

def sumMult3n5(N):
    return arithmeticProgress(3, N) + arithmeticProgress(5, N) - arithmeticProgress(3 * 5, N);

print(sumMult3n5(1000))