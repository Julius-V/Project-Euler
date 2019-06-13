from math import log, floor


def sieve_sundaram(upper_limit):
        sieve_limit = floor((upper_limit - 2) / 2)
        nums = [True] * (sieve_limit + 1)
        for i in range(1, floor(sieve_limit / 2)):
            for j in range(1, floor(sieve_limit / 2)):
                num = i + j + 2 * i * j
                if num <= sieve_limit:
                    if nums[num]:
                        nums[num] = False
                else:
                    break
        return [2 * i + 1 for i in range(0, sieve_limit) if nums[i]]

def nth_prime(n):
        return sieve_sundaram(n * log(n) + n * log(log(n)))[n - 1]

print(nth_prime(10001))