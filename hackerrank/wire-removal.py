# HackerRank problem Wire Removal
# https://www.hackerrank.com/contests/hourrank-24/challenges/wire-removal/problem 

# Solution modified from C++ editorial. In progress.
from collections import defaultdict

def dfs(node, depth, n, tree, subtree_sizes, visited):
    global total_expected
    global total_depth
    visited[node] = True
    subtree_sizes[node] = 1
    for child in tree[node]:
        if not visited[child]:
            dfs(child, depth + 1, n, tree, subtree_sizes, visited)
            subtree_sizes[node] += subtree_sizes[child]
    if node != 1:
        total_expected += depth * (n - subtree_sizes[node])
        total_depth += depth
        
n = int(raw_input())
subtree_sizes = defaultdict(int)
total_expected = 0
total_depth = 0
visited = [False] * (n + 1)

tree = defaultdict(list)
for i in xrange(n - 1):
    u, v = map(int, raw_input().strip().split())
    tree[u].append(v)
    tree[v].append(u)
dfs(1, 0, n, tree, subtree_sizes, visited)
print total_expected / float(total_depth)