from collections import defaultdict
def is_connected(edges):
    if len(edges) == 0:
        return True
    connections = defaultdict(list)
    for edge in edges:
        connections[edge[0]].append(edge[1])
        connections[edge[1]].append(edge[0])
    seen = set()
    seen.add(edges[0][0])
    queue = [edges[0][0]]
    while len(queue) > 0:
        current = queue.pop()
        new_edges = [edge for edge in connections[current] if edge not in seen]
        seen.update(new_edges)
        queue.extend(new_edges)
    return len(edges) == len(seen)

def bfs(tree, target):
    queue = [tree]
    while len(queue) > 0:
        current = queue.pop(0)
        if current.value == target:
            return True
        queue.extend(child for child in current.children if child is not None)
    return False

from collections import defaultdict
def is_connected(edges):
    if len(edges) == 0:
        return True
    connections = defaultdict(list)
    for edge in edges:
        connections[edge[0]].append(edge[1])
        connections[edge[1]].append(edge[0])
    seen = set()
    seen.add(edges[0][0])
    queue = [edges[0][0]]
    while len(queue) > 0:
        current = queue.pop()
        new_edges = [x for x in connections[current] if x not in seen]
        seen.update(new_edges)
        queue.extend(new_edges)
    return len(seen) == len(edges)

from collections import defaultdict
def connected_components(edges):
    components = []
    connections = defaultdict(list)
    for edge in edges:
        connections[edge[0]].append(edge[1])
        connections[edge[1]].append(edge[0])
    seen = set()
    for point in connections:
        queue = connections[point]
        if point not in seen:
            components.append([point])
            seen.add(point)
        while len(queue) > 0:
            current = queue.pop()
            components[-1].append(current)
            new_edges = [x for x in connections[current] if x not in seen]
            seen.update(new_edges)
            queue.extend(new_edges)
    return components





