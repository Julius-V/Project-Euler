# Computing the largest prime factor of n
def max_prime_factor(n):
    p = 2
    largest = None
    # Considering all potential possible prime divisors of n
    while p * p <= n:
        # If found one, keep dividing n by p until they become coprime
        while n % p == 0:
            n /= p
            largest = p
        p += 1
    # If n > 1, it must be that p * p > n = prime_number * 1
    return n if n > 1 else largest


print(max_prime_factor(600851475143))
