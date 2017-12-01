# HackerRank problem Wire Removal
# https://www.hackerrank.com/contests/hourrank-24/challenges/wire-removal/problem 

# Note: This solution does not currently pass the test cases.
#   Some of the nodes are discovered before their parents, causing KeyErrors.
from collections import defaultdict

if __name__ == "__main__":
    n = int(raw_input().strip())
    tree = defaultdict(list)
    edges = []
    depths = {1:0}
    for _ in xrange(n-1):
        x, y = map(int, raw_input().strip().split(' '))
        edges.append((x, y))
        tree[x].append(y)
        depths[y] = depths[x] + 1
    total_expected = 0.0
    total_depth = float(sum(depths.values()))
    subtree_sizes = {}
    for node in sorted(depths, key=lambda x: depths[x], reverse=True):
        subtree_size = 1 + sum(subtree_sizes[x] for x in tree[node])
        subtree_sizes[node] = subtree_size
        edge_prob = depths[node] / total_depth
        total_expected += edge_prob * (n - subtree_size)
    print total_expected