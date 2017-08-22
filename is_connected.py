from collections import defaultdict

def is_connected(edges):
    """Returns True if the edges represent one connected chunk.

    Args:
        edges: list of length-two lists or tuples.
            For example, [1, 2] indicates an edge from vertex "1" to vertex "2".
            Vertices must be hashable.

    Returns:
        True if the edges are a single connected chunk, False otherwise.
        Returns True if edges is empty.
    """
    if not edges:
        return True # or False, depending on specification
    graph = defaultdict(list)
    for start, end in edges:
        graph[start].append(end)
        graph[end].append(start)
    # Initialize queue with arbitrary edge
    queue = [edges[0][0]]
    seen = set()
    while queue:
        current = queue.pop(0)
        queue.extend(x for x in graph[current] if x not in seen)
        seen.add(current) # Optional
        seen.update(graph[current])
    return len(seen) == len(graph)
