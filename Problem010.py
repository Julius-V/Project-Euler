from math import log, floor


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
        return [2 * i + 1 for i in range(0, sieve_limit) if nums[i]]


# Summing all the primes up to 2 million and adding 2 as the sieve of Sundaram skips it
print(sum(sieve_sundaram(2000000)) + 2)
