def frog(steps, jumps, cache=None):
    if steps < 0:
        return 0
    if steps == 0 or steps == 1:
        return 1
    if cache is None:
        cache = {}
    elif steps in cache:
        return cache[steps]
    partial_result = sum(frog(steps-x, jumps, cache) for x in xrange(1, jumps + 1))
    cache[steps] = partial_result
    return partial_result



