def get_rank(array, k, start=0, end=None):
    if end is None:
        end = len(array) - 1
    if k < 0 or k > end - start:
        raise IndexError
    if k == 0 and start == end:
        return array[start]
    pivot_pos = partition(array, start, end)
    left_size = pivot_pos - start
    if k == left_size:
        return array[pivot_pos]
    if k < left_size:
        return get_rank(array, k, start, pivot_pos - 1)
    else:
        return get_rank(array, k - left_size - 1, pivot_pos + 1, end)

def partition(array, start, end):
    pivot = array[end]
    swap = start
    for i in xrange(start, end):
        if array[i] <= pivot:
            array[i], array[swap] = array[swap], array[i]
            swap += 1
    array[end], array[swap] = array[swap], array[end]
    return swap

import random
def quicksort(array, start=0, end=None):
    if end is None:
        end = len(array) - 1
    if start >= end:
        return
    pivot_pos = partition(array, start, end)
    quicksort(array, start, pivot_pos - 1)
    quicksort(array, pivot_pos + 1, end)

def quicksort(array, start=0, end=None):
    if end is None:
        end = len(array) - 1
    if start >= end:
        return
    left, right = partition(array, start, end)
    quicksort(array, start, right)
    quicksort(array, left, end)

def partition(array, start, end):
    pivot = random.choice(array[start:end+1])
    left = start
    right = end
    while left <= right:
        while array[left] < pivot:
            left += 1
        while array[right] > pivot:
            right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
            right -= 1
            left += 1
    return left, right

def partition(array, start, end):
    pivot = array[end]
    swap = start
    for i in xrange(start, end):
        if array[i] <= pivot:
            array[i], array[swap] = array[swap], array[i]
            swap += 1
    array[end], array[swap] = array[swap], array[end]
    return swap

def frog(steps, jumps, cache=None):
    if cache is None:
        cache = {}
    elif steps in cache:
        return cache[steps]
    if steps < 0:
        return 0
    if steps == 0 or steps == 1:
        return 1
    result = sum(frog(steps-x, jumps, cache) for x in xrange(1, jumps + 1))
    cache[steps] = result
    return result

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
        queue = [remaining_vertices.pop()]
        seen = set()
        while len(queue) > 0:
            current = queue.pop()
            seen.add(current)
            new_edges = [x for x in graph[current] if x not in seen]
            seen.update(new_edges)
            queue.extend(new_edges)
        remaining_vertices = [x for x in remaining_vertices if x not in seen]
        components.append(list(seen))
    return len(components)


def components(edges):
    if not edges:
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
            current = queue.pop()
            seen.add(current)
            new_edges = [x for x in graph[current] if x not in seen]
            seen.update(new_edges)
            queue.extend(new_edges)
        components.append(list(seen))
        remaining_edges = [x for x in remaining_edges if x not in seen]
    return len(components)
