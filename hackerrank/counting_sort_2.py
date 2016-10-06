import sys

def counting_sort(arr):
    """Hackerrank 'Counting Sort 2'."""
    # Given that numbers are integers in range 0 <= x < 100
    counts = [0 for _ in xrange(100)]
    for num in arr:
        counts[num] += 1
    sorted_arr = []
    for i in xrange(100):
        sorted_arr.extend([i] * counts[i])
    print " ".join(map(str, sorted_arr))
        
n = input()
arr = map(int, sys.stdin.read().split())
counting_sort(arr)
