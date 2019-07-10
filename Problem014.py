# Lengths of all Collatz sequences starting from 1, ..., n
def collatz(n):
    lens = [0] * n
    for i in range(1, n + 1):
        seq = [i]
        next_i = i
        while next_i != 1:
            next_i = next_i // 2 if next_i % 2 == 0 else 3 * next_i + 1
            seq.append(next)
            if next_i <= n:
                if lens[next_i - 1] != 0:
                    break
        if next_i == 1:
            lens[i - 1] = len(seq)
        else:
            lens[i - 1] = len(seq) + lens[next_i - 1] - 1
    return lens.index(max(lens)) + 1


print(collatz(1000000))
