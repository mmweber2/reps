def frog(steps, jumps):
    if steps < 0:
        return 0
    if steps == 0 or jumps == 1:
        return 1
    return sum(frog(steps-x, jumps) for x in xrange(1, jumps + 1))

from collections import defaultdict
def is_connected(edges):
    if len(edges) == 0:
        return True
    connections = defaultdict(list)
    for edge in edges:
        connections[edge[0]].append(edge[1])
        connections[edge[1]].append(edge[0])
    queue = [edges[0][0]]
    seen = set()
    while len(queue) > 0:
        current = queue.pop()
        new_edges = [edge for edge in connections[current] if edge not in seen]
        seen.update(new_edges)
        queue.extend(new_edges)
    return len(seen) == len(connections)
