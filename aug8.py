from collections import defaultdict

def is_connected(edges):
    if not edges:
        return True
    graph = defaultdict(list)
    for edge in edges:
        start, end = edge
        graph[start].append(end)
        graph[end].append(start)
    seen = set()
    queue = [edges[0][0]]
    seen.add(edges[0][0])
    while len(queue) > 0:
        current = queue.pop(0)
        new_edges = [x for x in graph[current] if x not in seen]
        seen.update(new_edges)
        queue.extend(new_edges)
    return len(seen) == len(graph)

def permute(s):
    if len(s) <= 1:
        return [s]
    perms = []
    for i in xrange(len(s)):
        current = s[i]
        for perm in permute(s[:i] + s[i+1:]):
            perms.append(current + perm)
    return perms

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
    array[end], array[swap_pos] = array[swap_pos], array[end]
    return swap_pos

import random
def quicksort(array, start=0, end=None):
    if not array:
        return array
    if end == None:
        end = len(array) - 1
    if start > end:
        raise IndexError
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

def permute(s):
    if len(s) <= 1:
        return set(s)
    perms = set()
    for i in xrange(len(s)):
        current = s[i]
        for perm in permute(s[:i] + s[i+1:]):
            perms.add(current + perm)
    return perms

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
    array[swap], array[end] = array[end], array[swap]
    return swap

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

def quicksort(array, start=0, end=None):
    if end is None:
        end = len(array) - 1
    if start >= end:
        return
    pivot = array[end]
    swap = start
    for i in xrange(start, end):
        if array[i] <= pivot:
            array[i], array[swap] = array[swap], array[i]
            swap += 1
    array[swap], array[end] = array[end], array[swap]
    quicksort(array, start, swap - 1)
    quicksort(array, swap + 1, end)

def quicksort(array, start=0, end=None):
    if end is None:
        end = len(array) - 1
    if start >= end:
        return
    swap = partition(array, start, end)
    quicksort(array, start, swap - 1)
    quicksort(array, swap + 1, end)

def partition(array, start, end):
    pivot = array[end]
    swap = start
    for i in xrange(start, end):
        if array[i] <= pivot:
            array[i], array[swap] = array[swap], array[i]
            swap += 1
    array[swap], array[end] = array[end], array[swap]
    return swap

def quicksort(array, start=0, end=None):
    if end is None:
        end = len(array) - 1
    if start >= end:
        return
    pivot_pos = partition(array, start, end)
    quicksort(array, start, pivot_pos - 1)
    quicksort(array, pivot_pos + 1, end)

def partition(array, start, end):
    swap = start
    pivot = array[end]
    for i in xrange(start, end):
        if array[i] <= pivot:
            array[i], array[swap] = array[swap], array[i]
            swap += 1
    array[swap], array[end] = array[end], array[swap]
    return swap
