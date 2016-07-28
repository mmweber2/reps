from collections import defaultdict
def is_connected(edges):
    if len(edges) == 0:
        return True
    connections = defaultdict(list)
    for edge in edges:
        start, end = edge
        connections[start].append(end)
        connections[end].append(start)
    seen = set()
    seen.add(edges[0][0])
    queue = [edges[0][0]]
    while len(queue) > 0:
        current = queue.pop()
        new_edges = [x for x in connections[current] if x not in seen]
        seen.update(new_edges)
        queue.extend(new_edges)
    return len(seen) == len(connections)

# import
# Did not get correct.
def components(edges):
    if len(edges) < 2:
        return 1
    connections = defaultdict(list)
    for edge in edges:
        start, end = edge
        connections[start].append(end)
        connections[end].append(start)
    components = []
    point_list = list(connections)
    while len(point_list) > 0:
        queue = [point_list.pop()]
        seen = set()
        while len(queue) > 0:
            current = queue.pop()
            seen.add(current)
            new_edges = [x for x in connections[current] if x not in seen]
            seen.update(new_edges)
            queue.extend(new_edges)
        remaining_edges = [x for x in point_list if x not in seen]
        components.append(list(seen))
    return len(components)

# Import
def dfs(edges, target):
    connections = defaultdict(list)
    for edge in edges:
        start, end = edge
        connections[start].append(end)
        connections[end].append(start)
    stack = [edges[0][0]]
    seen = set()
    seen.add(edges[0][0])
    while len(stack) > 0:
        current = stack.pop()
        if current == target:
            return True
        new_edges = [x for x in connections[current] if x not in seen]
        stack.extend(new_edges)
        seen.update(new_edges)
    return False








