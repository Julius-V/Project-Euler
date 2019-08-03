from math import floor, sqrt


# Using the sieve of Sundaram to generate primes up to upper_limit (without 2)
def sieve_sundaram(upper_limit):
    sieve_limit = floor((upper_limit - 2) / 2)
    nums = [True] * (sieve_limit + 1)
    nums[0] = False
    for i in range(1, floor(sieve_limit / 2)):
        for j in range(1, floor(sieve_limit / 2)):
            num = i + j + 2 * i * j
            if num <= sieve_limit:
                if nums[num]:
                    nums[num] = False
            else:
                break
    return [2 * i + 1 for i in range(sieve_limit) if nums[i]]


# Checking if n is a prime
def is_prime(n, primes):
    if n < 10000:
        return n in primes
    else:
        d = 2
        while d <= floor(sqrt(n)):
            if n % d == 0:
                return False
            d += 1
        return True


# Finding the lowest sum for a set of five primes for which any two primes
# concatenate to produce another prime.
# Assuming that the first found tuple is the solution.
def smallest_prime_set():
    primes = sieve_sundaram(10000)
    pn = len(primes)
    for p1 in range(pn):
        s1 = str(primes[p1])
        for p2 in range(p1, pn):
            s2 = str(primes[p2])
            if not (is_prime(int(s1 + s2), primes) and is_prime(int(s2 + s1), primes)):
                continue
            for p3 in range(p2, pn):
                s3 = str(primes[p3])
                if not (is_prime(int(s1 + s3), primes) and is_prime(int(s2 + s3), primes) and
                        is_prime(int(s3 + s1), primes) and is_prime(int(s3 + s2), primes)):
                    continue
                for p4 in range(p3, pn):
                    s4 = str(primes[p4])
                    if not (is_prime(int(s1 + s4), primes) and is_prime(int(s2 + s4), primes) and
                            is_prime(int(s3 + s4), primes) and is_prime(int(s4 + s1), primes) and
                            is_prime(int(s4 + s2), primes) and is_prime(int(s4 + s3), primes)):
                        continue
                    for p5 in range(p4, pn):
                        s5 = str(primes[p5])
                        if not (is_prime(int(s1 + s5), primes) and is_prime(int(s2 + s5), primes) and
                                is_prime(int(s3 + s5), primes) and is_prime(int(s4 + s5), primes) and
                                is_prime(int(s5 + s1), primes) and is_prime(int(s5 + s2), primes) and
                                is_prime(int(s5 + s3), primes) and is_prime(int(s5 + s4), primes)):
                            continue
                        return int(s1) + int(s2) + int(s3) + int(s4) + int(s5)


print(smallest_prime_set())
