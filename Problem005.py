def lcm(a, b):
    m, n = a, b
    while m != n:
        if m > n:
            n = n + b
        else:
            m = m + a
    return m

def lcmMulti(nums):
    if len(nums) > 2:
        return lcm(nums[0], lcmMulti(nums[1::]))
    else:
        return lcm(nums[0], nums[1])

print(lcmMulti(range(1, 20 + 1)))