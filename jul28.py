def frog(steps, jumps, cache=None):
    if steps < 0:
        return 0
    if steps == 0 or steps == 1:
        return 1
    if cache is None:
        cache = {}
    elif steps in cache:
        return cache[steps]
    result = sum(frog(steps-x, jumps, cache) for x in xrange(1, jumps + 1))
    cache[steps] = result
    return result

from collections import defaultdict
def components(edges):
    if len(edges) == 0:
        return 0
    graph = defaultdict(list)
    for edge in edges:
        start, end = edge
        graph[start].append(end)
        graph[end].append(start)
    components = []
    remaining_vertices = list(graph)
    while len(remaining_vertices) > 0:
        seen = set()
        queue = [remaining_vertices.pop()]
        while len(queue) > 0:
            current = queue.pop(0)
            seen.add(current)
            new_edges = [x for x in graph[current] if x not in seen]
            seen.update(new_edges)
            queue.extend(new_edges)
        components.append(list(seen))
        remaining_vertices = [x for x in remaining_vertices if x not in seen]
    return len(components)

def perms(s):
    if len(s) <= 1:
        return [s]
    partials = []
    for i in xrange(len(s)):
        current = s[i]
        for perm in perms(s[:i] + s[i+1:]):
            partials.append(current + perm)
    return partials

def perms2(s):
    if len(s) <= 1:
        return set(s)
    perms = set()
    for i in xrange(len(s)):
        current = s[i]
        for perm in perms2(s[:i] + s[i+1]):
            perms.add(current + perm)
    return perms




