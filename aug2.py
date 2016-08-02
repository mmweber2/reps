def perms(s):
    if len(s) <= 1:
        return [s]
    permutations = []
    for i in xrange(len(s)):
        current = [s[i]]
        for perm in perms(s[:i] + s[i+1:]):
            permutations.append(current + perm)
    return permutations

import random
def quicksort(array, start=0, end=None):
    if end is None:
        end = len(array) - 1
    if start >= end:
        return array
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
            left += 1
            right -= 1
    quicksort(array, start, right)
    quicksort(array, left, end)
    
def perms(s):
    if len(s) <= 1:
        return [s]
    done = []
    for i in xrange(len(s)):
        current = s[i]
        for perm in perms(s[:i] + s[i+1:]):
            done.append(current + perm)
    return done

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
    # optional
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
        seen = ()
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

import random
def quicksort(array, start=0, end=None):
    if end is None:
        end = len(array) - 1
    if start >= end:
        return array
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
            left += 1
            right -= 1
    quicksort(array, start, right)
    quicksort(array, left, end)
    return quicksort

def perms(s):
    if len(s) <= 1:
        return [s]
    done = []
    for i in xrange(len(s)):
        current = [s[i]]
        for perm in perms(s[:i] + s[i+1:]):
            done.append(current + perm)
    return done

def permute(s):
    if len(s) <= 1:
        return set(s)
    perms = set()
    for i in xrange(len(s)):
        for perm in permute(s[:i] + s[i+1:]):
            perms.add(s[i] + perm)
    return perms

from collections import defaultdict
def components(edges):
    graph = defaultdict(list)
    for edge in edges:
        start, end = edge
        graph[start].append(end)
        graph[end].append(start)
    components = []
    remaining = list(graph)
    while len(remaining) > 0:
        seen = set()
        queue = [remaining.pop()]
        whle len(queue) > 0:
            current = queue.pop(0)
            seen.add(current)
            new_edges = [x for x in graph[current] if x not in seen]
            seen.update(new_edges)
            queue.extend(new_edges)
        components.append(list(seen))
        remaining = [x for x in remaining if x not in seen]
    return len(components)

def permute(s):
    if len(s) <= 1:
        return set(s)
    perms = set()
    for i in xrange(len(s)):
        for perm in permute(s[:i] + s[i+1:]):
            perms.add(s[i] + perm)
    return perms

from collections import defaultdict
def components(edges):
    graph = defaultdict(list)
    for edge in edges:
        start, end = edge
        graph[start].append(end)
        graph[end].append(start)
    components = []
    remaining = list(graph)
    while len(remaining) > 0:
        seen = set()
        queue = [remaining.pop()]
        while len(queue) > 0:
            current = queue.pop(0)
            seen.add(current)
            new_edges = [x for x in graph[current] if x not in seen]
            seen.update(new_edges)
            queue.extend(new_edges)
        components.append(list(seen))
        remaining = [x for x in remaining if x not in seen]
    return len(remaining)









