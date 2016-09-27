# Hackerrank Save the Prisoner problem.

import sys

def find_poisoned(num_pri, num_sweets, starting_id):
    poisoned = (starting_id + num_sweets - 1) % num_pri
    if poisoned == 0:
        print num_pri
        return
    print poisoned
        
num_tests = int(sys.stdin.readline())
for _ in xrange(num_tests):
    n, m, t = (int(x) for x in sys.stdin.readline().split())
    find_poisoned(n, m, t)
