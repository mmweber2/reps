# Solution for HackerRank problem Mutual Indivisibility
# https://www.hackerrank.com/contests/hourrank-24/challenges/mutual-indivisibility/problem

# Adapted from editorial solution.

if __name__ == "__main__":
    t = int(raw_input().strip())
    for _ in xrange(t):
        a, b, x = map(int, raw_input().strip().split())
        # How many players are there before we reach player b / 2?
        set_size = min(b - a + 1, (b + 1) / 2)
        if x > set_size:
            # Not enough players in this range
            print -1
        else:
            # Print the last x players
            print " ".join(str(player) for player in xrange(b, b - x, -1))