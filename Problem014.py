# Lengths of all Collatz sequences starting from 1, ..., n
def collatz(n):
    lens = [0] * n
    for i in range(1, n + 1):
        seq = [i]
        next = i
        while next != 1:
            next = next // 2 if next % 2 == 0 else 3 * next + 1
            seq.append(next)
            if next <= n:
                if lens[next - 1] != 0:
                    break
        if next == 1:
            lens[i - 1] = len(seq)
        else:
            lens[i - 1] = len(seq) + lens[next - 1] - 1
    return lens.index(max(lens)) + 1


print(collatz(1000000))
