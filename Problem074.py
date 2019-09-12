from math import factorial


# Sum of factorials of digits of n
def sum_digit_factorials(n):
    return sum([factorial(int(i)) for i in str(n)])


# Counting how many chains, with a starting number below n, contain exactly s non-repeating terms
def counting_s_chains(n, s):
    terms = [0] * (10 * n)
    terms[0] = 2
    for i in range(1, n):
        seen = [i]
        for j in range(1, s):
            term = sum_digit_factorials(seen[-1])
            if term in seen:
                terms[i] = len(seen)
                break
            if terms[term] != 0:
                terms[i] = len(seen) + terms[term]
                break
            seen.append(term)
        if terms[i] == 0:
            terms[i] = 2 * s + 1
    return terms.count(s)


print(counting_s_chains(1000000, 60))
