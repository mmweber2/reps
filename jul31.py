def perm(s):
    if len(s) <= 1:
        return [s]
    perms = []
    for i in xrange(len(s)):
        current = [s[i]]
        for p in perm((s[:i] + s[i+1])):
            perms.append(current + p)
    return perms

from collections import defaultdict
def is_connected(edges):
    if len(edges) == 0:
        return True
    graph = defaultdict(list)
    for edge in graph:
        start, end = edge
        graph[start].append(end)
        graph[end].append(start)
    seen = ()
    queue = [edges[0][0]]
    while len(queue) > 0:
        current = queue.pop()
        new_edges = [x for x in graph[current] if x not in seen]
        seen.update(new_edges)
        queue.extend(new_edges)
    return len(seen) == len(graph)

