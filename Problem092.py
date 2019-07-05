def square_digit_chains():
    ends = [0] * 10000000
    for i in range(1, len(ends)):
        num = sum([int(k) ** 2 for k in str(i)])
        n = [i, num]
        while num not in [1, 89]:
            num = sum([int(k) ** 2 for k in str(n[len(n) - 1])])
            if ends[num - 1] in [1, 89]:
                num = ends[num - 1]
            n.append(num)
        for j in range(len(n)):
            ends[n[j] - 1] = num
    return ends.count(89)


print(square_digit_chains())
