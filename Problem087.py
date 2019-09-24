from math import floor, sqrt


# Using the sieve of Sundaram to generate primes up to upper_limit
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


# Finding how many numbers below k can be expressed as the sum of a prime square,
# prime cube, and prime fourth power
def prime_power_triple(k):
    primes = [2] + sieve_sundaram(sqrt(k) + 1)
    numbers = []
    for c in range(len(primes)):
        h = primes[c] ** 4
        if h > k:
            break
        for b in range(len(primes)):
            m = h + primes[b] ** 3
            if m > k:
                break
            for a in range(len(primes)):
                n = m + primes[a] ** 2
                if n > k:
                    break
                numbers.append(n)
    return len(set(numbers))


print(prime_power_triple(50000000))
