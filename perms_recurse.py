# Problem statement:
# Write a recursive function for generating all permutations
# of an input string, and return them as a set.
# Don't worry about time or space complexity, just make it recursive.

# The problem statement says to return the output as a set.
# This is not the most convenient way to work with the partial
# permutations, so I've created a wrapper method to convert it to a
# set at the end.
# This also allows us to check for an empty input string only once.
def perms(input_string):
    if len(input_string) == 0:
        return set()
    return set(perms_inner(input_string, 0))

def perms_inner(input_string, pos=0):
    # Only one item left
    if pos == len(input_string) -1:
        return [input_string[pos]]
    partials = (perms_inner(input_string, pos + 1))
    current_char = input_string[pos]
    perms = []
    for i in xrange(len(partials)):
        for j in xrange(len(partials[i])+1): # add current at the end too
            perms.append(partials[i][:j] + current_char + partials[i][j:])
    return perms


