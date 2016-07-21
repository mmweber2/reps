def frog(steps, jumps):
    if steps < 0:
        return 0
    if steps == 0 or steps == 1:
        return 1
    return sum([frog(steps-x, jumps) for x in xrange(1, jumps + 1)])

from collections import defaultdict
# In form (vertex1, vertex2)
def is_connected(edges):
    connected_to = defaultdict(list)
    for edge in edges:
        connected_to[edge[0]].append(edge[1])
        connected_to[edge[1]].append(edge[0])
    seen = set()
    # If all points are connected, we should be able to start from any point and reach all others
    queue = [edges[0][0]]
    while len(queue) > 0:
        current = queue.pop(0)
        seen.add(current)
        queue.extend(connected_to[current])
    if len(seen) < len(connected_to):
        return False
    return True



