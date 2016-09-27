# Hackerrank Strange Counter problem
def counter(time):
    current_time = 1
    current_val = 3
    cycle = 0
    while current_time < time:
        increment = 3 * (2**cycle)
        if time >= current_time + increment:
            # Skip ahead to next cycle
            cycle += 1
            current_time += increment
            current_val = 3 * (2**cycle)
        else:
            current_val -= (time - current_time)
            current_time = time # or just break
    print current_val 
