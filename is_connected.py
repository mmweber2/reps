from collections import defaultdict

def is_connected(edges):
    if not edges:
        return True # or False, depending on specification
    graph = defaultdict(list)
    for start, end in edges:
        graph[start].append(end)
        graph[end].append(start)
    # Initialize queue with arbitrary edge
    queue = [edges[0][0]]
    seen = set()
    while queue:
        current = queue.pop(0)
        queue.extend(x for x in graph[current] if x not in seen)
        seen.update(graph[current])
    return len(seen) == len(connected_to)
