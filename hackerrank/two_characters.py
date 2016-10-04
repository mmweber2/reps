import sys
import re
from collections import Counter

def make_t_string(s):
    """For a given string, finds the length of its longest t string.

    A t string is a string consisting of only two characters where the
        characters alternate.

    Prints the length of the longest t string that can be made from s,
        or 0 if there is no such string.
    """
    s = _strip_repeats(s)
    charset = set(s)
    charlist = list(charset)
    counts = Counter('s')
    possible_pairs = []
    for i in xrange(len(charset)):
        for j in xrange(i + 1, len(charset)):
            if 0 <= abs(counts[charlist[i]] - counts[charlist[j]]) <= 1:
                possible_pairs.append((charlist[i], charlist[j]))
    max_seen = 0
    for a, b in possible_pairs:
        t = "".join(re.findall('[' + a + b + ']+', s))
        # Verify that these two characters still alternate
        if re.search(a +'{2,}', t) is None and re.search(b +'{2,}', t) is None:
            max_seen = max(max_seen, len(t))
    print max_seen     
                                
def _strip_repeats(s):
    """Find and remove any adjacent identical characters."""
    if len(s) < 2:
        return s
    old_s = s
    for c in set(old_s):
        if re.search(c +'{2,}', s) is not None:
            # Character appears 2+ times in a row; remove it
            s = "".join(re.findall('[^' + c + ']', s))
    # Characters that were not adjacent may now be, so check again
    if len(s) < len(old_s):
        s = _strip_repeats(s)
    return s
