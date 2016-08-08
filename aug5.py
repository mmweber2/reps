def permute(s):
    if len(s) <= 1:
        return set(s)
    perms = set()
    for i in xrange(len(s)):
        current = s[i]
        for perm in permute(s[:i] + s[i+1:]):
            perms.add(current + perm)
    return perms

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
        return
    pivot = random.choice(array[start:end+1])
    left = start
    right = end
    while left <= right:
        while array[left] < pivot:
            left += 1
        while array[right] > pivot:
            right -= 1
        if left <= right:
            sequence[left], sequence[right] = sequence[right], sequence[left]
            left += 1
            right -= 1
    quicksort(sequence, start, right)
    quicksort(sequence, left, end)

def permute(s):
    if len(s) <= 1:
        return set(s)
    perms = set()
    for i in xrange(len(s)):
        for perm in permute(s[:i] + s[i+1:]):
            perms.add(s[i] + perm)
    return perms

    lesser = []
    greater = []
    for e in array:
        if e <= pivot:
            lesser.append(e)
        elif e > pivot:
            greater.append(e)
    quicksort(lesser)
    quicksort(greater)
    return lesser + greater

def quicksort(array, start=0, end=None):
    if end is None:
        end = len(array) - 1
    if start >= end:
        return
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

import random
def quicksort(array, start=0, end=None):
    if end is None:
        end = len(array) - 1
    if start >= end:
        return
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

def get_rank(array, k, start=0, end=None):
    if end is None:
        end = len(array) - 1
    if k < 0 or k > end - start:
        raise IndexError("invalid k")
    if start == end and k == 0:
        return array[start]
    abs_pivot = partition(array, start, end)
    left_size = abs_pivot - start
    if k == left_size:
       return array[abs_pivot]
   if k < left_size:
       return get_rank(array, k, start, abs_pivot - 1)
   else:
       return get_rank(array, k - left_size - 1, abs_pivot + 1, end)

def partition(array, start, end):
    pivot = array[end]
    swap_pos = start
    for i in xrange(start, end):
        if array[i] <= pivot:
            array[swap_pos], array[i] = array[i], array[swap_pos]
            swap_pos += 1
    array[swap_pos], array[end] = array[end], array[swap_pos]
    return swap_pos

def get_rank(array, k, start=0, end=None):
    if end is None:
        end = len(array) - 1
    if k < 0 or k > end - start:
        raise IndexError
    if start == end and k == 0:
        return array[start]
    abs_pos = partition(array, start, end)
    left_size = abs_pos - start
    if k == left_size:
        return array[abs_pos]
    if k < left_size:
        return get_rank(array, k, start, abs_pos - 1)
    else:
        return get_rank(array, k - left_size - 1, abs_pos + 1, end)

def partition(array, start, end):
    pivot = array[end]
    swap_pos = start
    for i in xrange(start, end):
        if array[i] <= pivot:
            array[swap_pos], array[i] = array[i], array[swap_pos]
            swap_pos += 1
    array[swap_pos], array[end] = array[end], array[swap_pos]
    return swap_pos

def get_rank(array, k, start=0, end=None):
    if end is None:
        end = len(array) - 1
    if k < 0 or k > end - start:
        raise IndexError
    if start == end and k == 0:
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
    swap_pos = start
    for i in xrange(start, end):
        if array[i] <= pivot:
            array[i], array[swap_pos] = array[swap_pos], array[i]
            swap_pos += 1
    array[swap_pos], array[end] = array[end], array[swap_pos]
    return swap_pos

def get_rank(array, k, start=0, end=None):
    if end is None:
        end = len(array) - 1
    if k < 0 or k > end - start:
        raise IndexError
    if start == end and k == 0:
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
    swap_pos = start
    for i in xrange(start, end):
        if array[i] <= pivot:
            array[i], array[swap_pos] = array[swap_pos], array[i]
            swap_pos += 1
    array[swap_pos], array[end] = array[end], array[swap_pos]
    return swap_pos
            
