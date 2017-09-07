def bsearchr(ints, target, start=0, end=None):
    if end is None:
        end = len(ints) - 1
    if start > end:
        return -1
    mid = (end - start) / 2 + start
    if ints[mid] == target:
        return mid
    if ints[mid] < target:
        return bsearchr(ints, target, mid + 1, end)
    return bsearchr(ints, target, start, mid - 1)

def bsearchi(ints, target):
    if not ints:
        return -1
    start = 0
    end = len(ints) - 1
    while start <= end:
        mid = (end + start) / 2
        if ints[mid] == target:
            return mid
        if ints[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1