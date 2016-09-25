# TODO: Improve with cacheing
def move(clouds, current=0, jumps=0):
    if current == n - 1:
        # Made it!
        return jumps
    if current >= len(clouds) or clouds[current] == 1:
        # Not possible to do this many jumps, so use as an error condition
        return len(clouds) + 1
    move_two = move(clouds, current + 2, jumps + 1)
    move_one = move(clouds, current + 1, jumps + 1)
    return min(move_two, move_one)
