# Hackerrank Super Reduced String problem.
import sys

def reduce_string(s):
    """Reduces a string as far as possible.

    An operation exists to reduce a string when two identical characters are
    adjacent to each other.
    Performs this operation until no more identical characters are adjacent to
    each other, or the string is empty.

    Args:
        s: a string of lowercase characters to reduce.

    Returns:
        A string of the remaining characters, or "Empty String" if there are no
            remaining characters.
    """
    result = ""
    pos = 1
    while pos <= len(s):
        while pos < len(s) and s[pos - 1] == s[pos]:
            # 'Remove' these two characters
            pos += 2
        if pos <= len(s):
            # Add remaining unmatched character
            result += s[pos - 1]
        pos += 1
    if len(result) < len(s):
        result = reduce_string(result)
    return "Empty String" if len(result) == 0 else result

s = sys.stdin.read()
print reduce_string(s)
