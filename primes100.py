# Write a function to print all of the prime numbers less than 100

def print_primes():
    primes = range(98) # 100, 99, and 98 cannot be prime
    # primes[0] is already 0, so just mark 1 as not prime
    primes[1] = 0
    # Primes less than 10
    for factor in (2, 3, 5, 7):
        for product in xrange(factor * 2, 98, factor):
            primes[product] = None
    for prime in primes:
        if prime:
            print prime

print_primes()