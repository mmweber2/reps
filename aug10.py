from collections import defaultdict

def components(edges):
    if not edges:
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
            current = queue.pop()
            seen.add(current)
            new_edges = unseen(graph[current], seen)
            seen.update(new_edges)
            queue.extend(new_edges)
        components.append(list(seen))
        remaining_vertices = unseen(remaining_vertices, seen)
    return len(components)

def unseen(array, seen_vertices):
    return [x for x in array if x not in seen_vertices]

