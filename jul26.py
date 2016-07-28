from collections import defaultdict
# This is slightly different from my accepted solution as far as
# seen.add(point) (in the other version, it has seen.add(current)),
# but I think this should still work because any new vertex will
# get added when it's part of new_edges, and the first one is added
# before the loop begins.
def components(edges):
    if len(edges) == 0:
        return 0
    connections = defaultdict(list)
    for edge in edges:
        start, end = edge
        connections[start].append(end)
        connections[end].append(start)
    components = []
    remaining_vertices = list(connections)
    while len(remaining_vertices) > 0:
        point = remaining_vertices.pop(0)
        queue = [point]
        seen = set()
        seen.add(point)
        while len(queue) > 0:
            current = queue.pop(0)
            new_edges = [x for x in connections[current] if x not in seen]
            seen.update(new_edges)
            queue.extend(new_edges)
        components.append(list(seen))
        remaining_vertices = [x for x in remaining_vertices if x not in seen]
    return len(components)


