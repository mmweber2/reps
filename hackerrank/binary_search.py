# Submission for Intro to Tutorial Challenges on Hackerrank.
# Binary search is not necessary for this problem, but I wanted to practice
# it anyway rather than doing a linear search, since the data was already
# sorted.

# In this problem, it is given that target exists in the array exactly once.

def binary_search(target, array):
    start = 0
    end = len(array)
    while start < end:
        mid = (end - start) / 2 + start
        if array[mid] == target:
            print mid
            return
        if array[mid] < target:
            start = mid
        else:
            end = mid
