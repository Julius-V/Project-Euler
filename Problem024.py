from math import factorial


# Finding the nth lexicographic permutation of 0, 1, ..., 9
def nth_lexi_permutation(n):
    nums = list(range(0, 10))
    k = ''
    for i in range(10):
        prod = factorial(9 - i)
        if n % prod > 0:
            idx = n // prod
        else:
            idx = n // prod - 1
        k += str(nums[idx])
        del nums[idx]
        n = n % prod
    return k


print(nth_lexi_permutation(1000000))
