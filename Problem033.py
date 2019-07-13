# Finding all digit cancelling fractions
def digit_cancelling_fractions():
    o_a = 1
    o_b = 1
    for a in range(1, 10):
        for b in range(a + 1, 10):
            for c in range(1, 10):
                # ac / bc
                opt_1 = (10 * a + c) / (10 * b + c)
                # ac / cb
                opt_2 = (10 * a + c) / (10 * c + b)
                # ca / bc
                opt_3 = (10 * c + a) / (10 * b + c)
                # ca / cb
                opt_4 = (10 * c + a) / (10 * c + b)
                if a / b in [opt_1, opt_2, opt_3, opt_4]:
                    o_a *= a
                    o_b *= b
    return o_a / o_b


print(digit_cancelling_fractions())
