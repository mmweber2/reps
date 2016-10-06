import sys
import string

def is_pangram(s):
    """Prints 'pangram' if s is a pangram and 'not pangram' otherwise."""
    uniques = set(s.lower())
    # It is given in the problem statement that s contains only uppercase
    #   letters, lowercase letters, and spaces.
    expected = 27 if " " in uniques else 26 
    print "pangram" if len(uniques) == expected else "not pangram"

def is_pangram2(s):
    """Alternate version allowing for other non-space characters."""
    uniques = sum(1 for c in set(s.lower()) if c in string.ascii_lowercase)
    print "pangram" if uniques == 26 else "not pangram"

s = sys.stdin.read()
is_pangram(s)

