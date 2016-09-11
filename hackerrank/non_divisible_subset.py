from collections import defaultdict
def non_divisible_subset(numbers, k):
    """Find the maximum non divisible subset size for numbers.

    Given a set of unique integers, return the size of the largest subset such
    that no two numbers in the subset sum to a number evenly divisible by k.
    """
    count = 0
    mods_to = defaultdict(int)
    for number in numbers:
        mods_to[number % k] += 1
    for i in xrange(k / 2 + 1):
        j = k - i
        if i == 0 and mods_to[0]:
            count += 1
        elif i == j and mods_to[i]:
            count += 1
        else:
            count += max(mods_to[i], mods_to[j])
    return count

print "Expected: 3"
print non_divisible_subset([1, 2, 3, 4], 3)
print "Expected: 3"
print non_divisible_subset([1, 2, 6, 4], 4)


