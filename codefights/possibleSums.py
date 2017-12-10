def possibleSums(coins, quantity):
    sums = set()
    sums.add(0)
    for coin, quant in zip(coins, quantity):
        new_sums = set() # Don't confuse new and old values
        for coin_total in xrange(0, (coin * quant) + 1, coin):
            for s in sums:
                new_sums.add(s + coin_total)
        sums = new_sums
    return len(sums) - 1 # Account for 0