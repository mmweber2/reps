# Problem statement:
# Write a recursive function for generating all permutations
# of an input string, and return them as a set.
# Don't worry about time or space complexity, just make it recursive.

def perms(input_string):
    if len(input_string) <= 1:
        return set(input_string)
    results = set()
    for i in xrange(len(input_string)):
        current = input_string[i]
        for perm in perms(input_string[:i] + input_string[i+1:]):
            results.add(current + perm)
    return results

# Non-set version
def perms_partial2(input_string):
    if len(input_string) <= 1:
        return [input_string]
    perms = []
    for i in xrange(len(input_string)):
        current = input_string[i]
        for perm in perms_partial2(input_string[:i] + input_string[i+1:]):
            # Or (current + perm)
            perms.append(perm + current)
    return perms

# Alternate versions:

# The problem statement says to return the output as a set.
# This is not the most convenient way to work with the partial
# permutations, so I've created a wrapper method to convert it to a
# set at the end.
# This also allows us to check for an empty input string only once.
def perms_outer(input_string):
    if len(input_string) == 0:
        return set()
    return perms_inner(input_string, 0)

# To be used with wrapper perms_outer
def perms_inner(input_string, pos):
    # Only one item left
    if pos == len(input_string) -1:
        return [input_string[pos]]
    partials = (perms_inner(input_string, pos + 1))
    current_char = input_string[pos]
    new_perms = []
    for i in xrange(len(partials)):
        for j in xrange(len(partials[i])+1): # add current at the end too
            new_perms.append(partials[i][:j] + current_char + partials[i][j:])
    return new_perms

# Alternate version that modifies the string and returns a list
def perms_partial(input_string):
    if len(input_string) <= 1:
        return [input_string]
    partials = perms_partial(input_string[1:])
    current_char = input_string[0]
    new_perms = []
    for i in xrange(len(partials)):
        for j in xrange(len(partials[i])+1):
            new_perms.append(partials[i][:j] + current_char + partials[i][j:])
    return new_perms






