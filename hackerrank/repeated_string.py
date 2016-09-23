# When repeating string sinfinitely many times, return the number of 'a'
# characters in the first chars_allowed characters of the infinite string.
def repeated_string(s, chars_allowed):
    if chars_allowed <= len(s):
        return s[:chars_allowed + 1].count("a")
    a_count = s.count("a") * (chars_allowed / len(s))
    a_count += s[:chars_allowed % len(s)].count("a") 
    return a_count
