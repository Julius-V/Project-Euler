

# Get the last m digits of 1^1 + 2^2 + ... + n^n
def last_m_to_n(m, n):
    return sum([i ** i for i in range(1, n + 1)]) % 10 ** m


print(last_m_to_n(10, 1000))
