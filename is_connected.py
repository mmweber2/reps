from collections import defaultdict

def is_connected(edges):
    if edges == []:
        return True
    connected_to = defaultdict(list)
    for edge in edges:
        connected_to[edge[0]].append(edge[1])
        connected_to[edge[1]].append(edge[0])
    queue = [edges[0][0]]
    seen = set()
    while len(queue) > 0:
        current = queue.pop(0)
        new_edges = [x for x in connected_to[current] if x not in seen]
        queue.extend(new_edges)
        seen.update(new_edges)
    if len(seen) < len(connected_to):
        return False
    return True
