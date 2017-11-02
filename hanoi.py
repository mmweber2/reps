class Tower(object):

    def __init__(self):
        self.discs = []

    def add(self, disc):
        if self.discs and self.discs[-1] <= disc:
            raise IndexError("Can't put a larger disc here")
        self.discs.append(disc)

    def move_discs(self, n, dest, temp):
        if not n:
            return
        # Move everything but the bottom disc to the temp spot
        self.move_discs(n - 1, temp, dest)
        # Move bottom disc to destination
        dest.discs.append(self.discs.pop())
        # Move the discs from the temp to the destination
        temp.move_discs(n - 1, dest, self)

def solve(num_discs):
    towers = [Tower() for i in xrange(3)]
    # Put all the discs on the first tower to start
    towers[0].discs = range(num_discs-1, -1, -1) 
    # Move everything from tower 0 to tower 2, with tower 1 as buffer
    towers[0].move_discs(num_discs, towers[2], towers[1])
    return towers


