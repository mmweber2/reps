# Hackerrank Strange Counter problem
def counter(time):
    current = 3
    while time > current:
        time -= current
        current *= 2
    print current - time + 1
