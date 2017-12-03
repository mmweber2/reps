# Solution for HackerRank problem Mutual Indivisibility
# https://www.hackerrank.com/contests/hourrank-24/challenges/mutual-indivisibility/problem

# Adapted from editorial solution.

if __name__ == "__main__":
    t = int(raw_input().strip())
    for _ in xrange(t):
        a, b, x = map(int, raw_input().strip().split())
        find_players(a, b, x)

def find_players(start, end, num_players):
    # How many players are there before we reach player (end / 2)?
    set_size = min(end - start + 1, (end + 1) / 2)
    if num_players > set_size:
        # Not enough players in this range
        print -1
    else:
        # Print the last num_players players
        print " ".join(str(x) for x in xrange(end, end - num_players, -1))