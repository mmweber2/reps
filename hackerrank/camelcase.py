import sys
import string

def count_words(s):
    """Counts the number of words in CamelCase s.

    The first letter of s is always lowercase, and the first letter of all
        other words in s are uppercase. All other letters of all words
        are lowercase.

    Args:
        s: string, in CamelCase form beginning with a lowercase letter.
            Must be at least one character long, and contains no non-letter
            characters.

    Returns:
        integer, the number of words in s.
    """
    upper = set(string.uppercase) # or string.ascii_uppercase
    print sum(1 for x in s if x in upper) + 1 # first word is not uppercase

s = raw_input().strip()
count_words(s)
