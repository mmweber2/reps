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
        queue.extend(new_edges)
        seen.update(new_edges)
    return len(seen) == len(connections)

def dfs(tree, target):
    if tree is None:
        return False
    if tree.value == target:
        return True
    return dfs(tree.left, target) or dfs(tree.right, target)

from collections import defaultdict
def is_connected(edges):
    if len(edges) == 0:
        return True
    connections = defaultdict(list)
    for edge in edges:
        connections[edge[0]].append([edge[1]])
        connections[edge[1]].append([edge[0]])
    seen = set()
    seen.add(edges[0][0])
    queue = [edges[0][0]]
    while len(queue) > 0:
        current = queue.pop()
        queue.extend([x for x in connections[current] if x not in seen])
        seen.update(connections[current])
    return len(seen) == len(connections)

# Bonus version: What if you can't use defaultdict?

def is_connected(edges):
    if len(edges) == 0:
        return True
    connections = {}
    for edge in edges:
        start, end = edge
        if start in connections:
            connections[start].append(end)
        else:
            connections[start] = [end]
        if end in connections:
            connections[end].append(start)
        else:
            connections[end] = [start]
    # exactly the same from here
    seen = set()
    seen.add(edges[0][0])
    queue = edges[0][0]
    while len(queue) > 0:
        current = queue.pop()
        queue.extend(x for x in connections[current] if x not in seen)
        seen.update(connections[current])
    return len(seen) == len(connections)

from collections import defaultdict
def components(edges):
    if len(edges) == 0:
        return 0
    connections = defaultdict(list)
    for edge in edges:
        start, end = edge
        connections[start].append(end)
        connections[end].append(start)
    components = 0
    vertex_list = list(connections)
    while len(vertex_list) > 0:
        seen = set()
        queue = [vertex_list.pop()]
        while len(queue) > 0:
            current = queue.pop()
            seen.add(current)
            queue.extend(x for x in connections[v] if x not in seen)
            seen.update(connections[v])
        vertex_list = [x for x in vertex_list if x not in seen]
        components += 1
    return components
        






