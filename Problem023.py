from math import sqrt, ceil


# The sum of proper divisors of n
def sum_pdivisors(n):
    s = 1
    for i in range(2, ceil(sqrt(n))):
        if n % i == 0:
            s += i + n // i
    if sqrt(n) == round(sqrt(n)):
        s += round(sqrt(n))
    return s


# Whether a number is abundant
def is_abundant(n):
    return sum_pdivisors(n) > n


# All the abundant numbers up to m
def abundant_numbers(m):
    out = []
    for i in range(2, m + 1):
        if is_abundant(i):
            out.append(i)
    return out


# Sum all the numbers that cannot be written as a sum of two abundant numbers
def sum_inabundables():
    upper_limit = 28123
    abundant = abundant_numbers(upper_limit)
    nums = [False] * upper_limit
    for i in range(len(abundant)):
        for j in range(i, len(abundant)):
            s = abundant[i] + abundant[j]
            if s <= upper_limit:
                nums[s - 1] = True
    return sum([(not nums[i]) * (i + 1) for i in range(len(nums))])


print(sum_inabundables())
