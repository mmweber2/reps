import sys
from itertools import groupby

def make_alternate(s):
    """Prints the number of characters to remove to make s alternate.

    Alternating character string examples include:
    A
    B
    ABA
    BA
    ABABAB

    It is given that s is a string at least one character long.
    """
    streak = 0
    for k, g in groupby(s):
        streak += len(k) 
    # We have found the number of alternating groups, so any characters
    # beyond that count must be duplicates.
    print len(s) - streak
        
# First input line is the number of test cases
# Following lines are test cases, one per line
n = input()
for _ in xrange(n):
    make_alternate(sys.stdin.readline().strip())
