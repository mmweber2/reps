def move(clouds, current=0, jumps=0, cache=None):
    if current == n - 1:
        # Made it!
        return jumps
    if current >= len(clouds) or clouds[current] == 1:
        return -1
    if cache is None:
        cache = {}
    elif current in cache:
        return cache[current]
    move_two = move(clouds, current + 2, jumps + 1)
    move_one = move(clouds, current + 1, jumps + 1)
    partial = move_one if move_two == -1 else move_two
    cache[current] = partial
    return partial
