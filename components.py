from collections import defaultdict
def connected_components(edges):
    connections = defaultdict(list)
    for edge in edges:
        connections[edge[0]].append(edge[1])
        connections[edge[1]].append(edge[0])
    components = []
    # Track unvisited edges in a list for easy iteration and modification
    remaining_edges = list(connections)
    while len(remaining_edges) > 0:
        queue = [remaining_edges.pop()]
        seen = set()
        while len(queue) > 0:
            current = queue.pop()
            seen.add(current)
            new_edges = [x for x in connections[current] if x not in seen]
            seen.update(new_edges)
            queue.extend(new_edges)
        # Don't consider edges in this component next time
        remaining_edges = [x for x in remaining_edges if x not in seen]
        components.append(list(seen))
    return len(components)





