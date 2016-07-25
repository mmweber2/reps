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

# If we have something that gives us the connected components,
# it would help to use those components and iterate through them
# looking for cycles.
def has_cycle(edges):
    # Since we don't want to have a single edge connecting two
    # vertices to count as a cycle, we'll only add each edge once.
    connections = defaultdict(list)
    for edge in edges:
        connections[edge[0]].append(edge[1])
    for edge in edges:
        # No need to look at the edge[1] values, because they'll
        # all be checked when traversing the paired edge[0]
        point = edge[0]
        seen = set()
        seen.add(point)
        stack = connections[point]
        while len(stack) > 0:
            current = stack.pop()
            if current in seen:
                return True
            seen.add(current)
            stack.extend(connections[current])
    return False
    
