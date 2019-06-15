# Least common multiple of integers a and b
def lcm(a, b):
    m, n = a, b
    while m != n:
        if m > n:
            n = n + b
        else:
            m = m + a
    return m


# Least common multiple of a list of integers nums
def lcm_multi(nums):
    if len(nums) > 2:
        return lcm(nums[0], lcm_multi(nums[1::]))
    else:
        return lcm(nums[0], nums[1])


print(lcm_multi(range(1, 20 + 1)))
