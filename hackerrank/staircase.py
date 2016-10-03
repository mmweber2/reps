import sys

def print_staircase(n):
    for i in xrange(1, n + 1):
        print " " * (n-i) + "#" * i 

n = int(raw_input().strip())
print_staircase(n)
