# Given a list of edges, return a list of connected components.

from collections import defaultdict
def get_components(edges):
    connections = defaultdict(list)
    for start, end in edges:
        connections[start].append(end)
        connections[end].append(start)
    components = []
    # Track unvisited vertices in a list for easy iteration and modification
    remaining_vertices = list(connections)
    while remaining_vertices:
        queue = [remaining_vertices.pop()]
        seen = set()
        while queue:
            current = queue.pop()
            # Optional, but avoids extra traversals
            seen.add(current)
            queue.extend(x for x in connections[current] if x not in seen)
            seen.update(connections[current])
        # Don't consider edges in this component next time
        remaining_vertices = [x for x in remaining_vertices if x not in seen]
        components.append(list(seen))
    return components

# Alternate version:
# Given a list of edges, count the number of connected components.
def count_components(edges):
    connections = defaultdict(list)
    for start, end in edges:
        connections[start].append(end)
        connections[end].append(start)
    count = 0
    # Track unvisited vertices in a list for easy iteration and modification
    remaining_vertices = list(connections)
    while remaining_vertices:
        queue = [remaining_vertices.pop()]
        seen = set()
        while queue:
            current = queue.pop()
            # Optional, but avoids extra traversals
            seen.add(current)
            queue.extend(x for x in connections[current] if x not in seen)
            seen.update(connections[current])
        # Don't consider edges in this component next time
        remaining_vertices = [x for x in remaining_vertices if x not in seen]
        components += len(seen)
    return components
