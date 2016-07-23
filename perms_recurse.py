# Write a recursive function for generating all permutations
# of an input string, and return them as a set.
# Don't worry about time or space complexity, just make it recursive.

# Note: Still in progress, incomplete
def perms(input_string, pos=0):
    # Only one item left
    if pos == len(input_string) -1:
        return input_string[pos]
    partials = [perms(input_string, pos + 1)]
    current_char = input_string[pos]
    for i in xrange(len(partials)):
        for j in xrange(len(partials[i])):
            partials.append(partials[i][:j] + current_char + partials[i][j:])
    return partials


