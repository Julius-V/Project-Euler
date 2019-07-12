# Cancelling all the powers of 2 and 5 from n
def off_2_and_5(n):
    while n % 2 == 0:
        n //= 2
    while n % 5 == 0:
        n //= 5
    return n


# Finding the recurring cycle length of 1 / n
def recurring_cycle_len(n):
    n = off_2_and_5(n)
    if n == 1:
        return 0
    m = 1
    while ((10 ** m) % n) != 1:
        m += 1
    return m


# Finding 1 / d with the longest recurring cycle length for d < k
def max_recurring_cycle_len(k):
    return max([recurring_cycle_len(n) for n in range(2, k)])


print(max_recurring_cycle_len(1000))
