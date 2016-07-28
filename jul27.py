from collections import defaultdict
def is_connected(edges):
    if len(edges) == 0:
        return True
    graph = defaultdict(list)
    for edge in edges:
        start, end = edge
        graph[start].append(end)
        graph[end].append(start)
    seen = set()
    queue = [edge[0][0]]
    while len(queue) > 0:
        current = queue.pop()
        new_edges = [x for x in graph[current] if x not in seen]
        seen.update(new_edges)
        queue.extend(new_edges)
    return len(seen) == len(graph)

def frog(steps, jumps):
    if steps < 0:
        return 0
    if steps == 0 or steps == 1:
        return 1
    return sum(frog(x, jumps) for x in xrange(1, jumps + 1))

def frog(steps, jumps, cache=None):
    if steps < 0:
        return 0
    if steps == 0 or steps == 1:
        return 1
    if cache is None:
        cache = {}
    elif steps in cache:
        return cache[steps]
    result = sum(frog(steps-x, jumps, cache) for x in xrange(1, jumps + 1)
    cache[steps] = result
    return result

def bfs(tree, target):
    queue = [tree]
    while len(queue) > 0:
        current = queue.pop(0)
        if current.value == target:
            return True
        queue.extend(current.children)
    return False

def dfs(tree, target):
    stack = [tree]
    while len(stack) > 0:
        current = stack.pop()
        if current.value == target:
            return True
        stack.extend(current.children)
    return False

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
    unused_vertices = list(graph)
    while len(unused_vertices) > 0:
        start = unused_vertices.pop(0)
        queue = [start]
        seen = set()
        seen.add(start)
        while len(queue) > 0:
            current = queue.pop(0)
            new_edges = [x for x in graph[current] if x not in seen]
            seen.update(new_edges)
            queue.extend(new_edges)
        components.append(list(seen))
        unused_vertices = [x for x in unused_vertices if x not in seen]
    return len(components)

def components(edges):
    if len(edges) == 0:
        return 0
    graph = defaultdict(list)
    for edge in edges:
        start, end = edge
        graph[start].append(end)
        graph[end].append(start)
    components = []
    remaining_edges = list(graph)
    while len(remaining_edges) > 0:
        queue = [remaining_edges.pop(0)]
        seen = set()
        while len(queue) > 0:
            current = queue.pop(0)
            seen.add(current)
            new_edges = [x for x in graph[current] if x not in seen]
            seen.update(new_edges)
            queue.extend(new_edges)
        components.append(list(seen))
        remaining_edges = [x for x in remaining_edges if x not in seen]
    return len(components)

def components(edges):
    if len(edges) == 0:
        return 0
    graph = defaultdict(list)
    for edge in edges:
        start, end = edge
        graph[start].append(end)
        graph[end].append(start)
    components = []
    remaining_edges = list(graph)
    while len(remaining_edges) > 0:
        seen = set()
        queue = [remaining_edges.pop(0)]
        while len(queue) > 0:
            current = queue.pop(0)
            seen.add(current)
            new_edges = [x for x in graph[current] if x not in seen]
            seen.update(new_edges)
            queue.extend(new_edges)
        components.append(list(seen))
        remaining_edges = [x for x in remaining_edges if x not in seen]
    return len(components)
            
            



