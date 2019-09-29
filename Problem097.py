

# - We wish to find 28433 * 2^7830457 + 1 mod 10^10
# - Note that 10^10 = 2^10 * 5^10 and 28433 * 2^7830457 mod 2^10 = 0
# - Now in 2^7830457 mod 5^10 note that 2 and 5 are relatively prime
# - and phi(5^10) = 5^10 * (1 - 1 / 5) = 4 * 5^9, where phi is the Euler's totient function.
# - Hence, by Fermat's little theorem, 2^7830457 mod 5^10 = 2^(7830457 mod (4 * 5^9)) mod 5^10
print((28433 * 2 ** (7830457 % (4 * 5 ** 9)) + 1) % 10000000000)
