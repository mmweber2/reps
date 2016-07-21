def frog(steps, jumps):
    if steps < 0:
        return 0
    if steps == 0 or steps == 1:
        return 1
    return sum(frog(steps-x, jumps) for x in xrange(1, jumps + 1))

# Cached:
def frog(steps, jumps, cache=None):
    if cache is None:
        cache = {}
    if steps < 0:
        return 0
    if steps == 0 or steps == 1:
        return 1
    if steps in cache:
        return cache[steps]
    partial_result = sum(frog(steps-x, jumps) for x in xrange(1, jumps + 1))
    cache[steps] = partial_result
    return partial_result

from collections import defaultdict
def is_connected(edge_list):
    if len(edge_list) == 0:
        return True # or False
    connections = defaultdict(list)
    for edge_pair in edge_list:
        connections[edge_pair[0]].append(edge_pair[1])
        connections[edge_pair[1]].append(edge_pair[0])
    queue = edge_list[0][0]
    seen = set()
    while len(queue) > 0:
        current = queue.pop()
        # This version adds each item as it is visited, which is worse than
        # adding them as they are discovered.
        # We can add the first node to the seen set right away, or let it get
        # added later when we explore any node attached to it.
        seen.add(current)
        queue.extend(point for point in connections[current] if point not in seen)
    return len(connections) == len(seen)

def frog(steps, jumps, cache=None):
    if steps < 0:
        return 0
    if steps == 0 or steps == 1:
        return 1
    if cache is None:
        cache = {}
    elif steps in cache:
        return cache[steps]
    partial_result = sum(frog(steps-x, jumps) for x in xrange(1, jumps + 1))
    cache[steps] = partial_result
    return partial_result

5, 2

4: call 1: sum(frog(3), frog(2))
3: call 2: sum(frog(2), frog(1))
2: call 3: sum(frog(1), frog(0))
1: call 4: (return)
0: call 5: (return)
