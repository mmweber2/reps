from collections import defaultdict

# Given a graph (in the form of (start, end) tuples)
# and a starting point, use DFS to look for a given point name.
# Return True if found and False otherwise.
def dfs_graph(edges, start, target):
    if len(edges) == 0:
        return False
    connections = defaultdict(list)
    for edge in edges:
        begin, end = edge
        connections[begin].append(end)
        connections[end].append(begin)
    stack = [start]
    seen = set()
    seen.add(start)
    while len(stack) > 0:
        current = stack.pop()
        if current == target:
            return True
        new_edges = [x for x in connections[current] if x not in seen]
        stack.extend(new_edges)
        seen.update(new_edges)
    return False

