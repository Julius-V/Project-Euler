# Counting the number of different ways 'amount' can be made using any number of coins
def coin_sums(amount, coins):
    s = 0
    if len(coins) == 0:
        return 0
    if amount % coins[0] == 0:
        s += 1
    for t in range(amount // coins[0] + (amount % coins[0] != 0)):
        s += coin_sums(amount - t * coins[0], coins[1:])
    return s


print(coin_sums(200, [200, 100, 50, 20, 10, 5, 2, 1]))
