def frog(steps, jumps):
    if steps < 0:
        return 0
    if steps == 0 or steps == 1:
        return 1
    return sum((frog(steps-x, jumps) for x in xrange(1, jumps + 1)))



