# Since phi(n) = n * prod_{p|n} (1 - 1 / p),
# we have that n / phi(n) = prod_{p|n} (1 - 1 / p)^{-1}.
#
# Hence, the solution is n = p_1 * ... * p_n <= 1000000,
# where p_i is the i-th prime number and n is as large as possible.


def largest_up_to_million(ps):
    p = ps[0]
    ps = ps[1:]
    while True:
        if p * ps[0] > 1000000:
            return p
        p *= ps[0]
        ps = ps[1:]


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
print(largest_up_to_million(primes))
