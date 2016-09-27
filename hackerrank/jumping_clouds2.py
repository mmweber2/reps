# Hackerrank Jumping on the Clouds: Revisited.


def jump_clouds(num_clouds, clouds, jump):
    energy_spent = 0
    current = 0
    while True:
        current = (current + jump) % num_clouds
        energy_spent += 3 if clouds[current] == 1 else 1
        if current == 0:
            print 100 - energy_spent
            return
