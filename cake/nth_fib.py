def nth_fib(n):
    """Returns the nth fibonacci number in a 0-indexed fibonacci series."""
    if n == 0:
        return 0
    two_ago = 0
    one_ago = 1
    result = 1
    while n > 1:
        result = two_ago + one_ago
        two_ago = one_ago
        one_ago = result
        n -= 1
    # Returns 1 if n is 1 
    return result
