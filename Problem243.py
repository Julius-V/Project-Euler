import numpy as np
# We are looking for the smallest such d that
# phi(d) / (d - 1) < 15499 / 94744, i.e.,
# d / (d - 1) * prod_{p|d} (1 - 1 / p)  < 15499 / 94744


# First we find such first primes p that prod_{p|d} (1 - 1 / p) < 15499 / 94744
# for the first time
def step_1(primes_list, thr):
    prod = 1
    p = 0
    while prod >= thr:
        prod *= 1 - 1 / primes_list[p]
        p += 1
    return [primes[0:p], prod]


# Now we look for such k that d = 2^k * step_1(primes, 15499 / 94744) would be the solution
def step_2(primes_list, thr):
    k = 0
    aux = step_1(primes_list, thr)
    prod = aux[1]
    d_init = np.prod(aux[0])
    o = d_init / (d_init - 1) * prod
    while o >= thr:
        k += 1
        o = 2 ** k * d_init / (2 ** k * d_init - 1) * prod
    return 2 ** k * d_init


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
print(step_2(primes, 15499 / 94744))
