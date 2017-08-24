'''
Based on a problem from HackerRank.

Input: An encoded string where 1 = a, 2 = b, and so on.
  For two-digit numbers (beginning with j = 10), a # follows the number,
  so j appears as 10# in the string.
  If a letter appears multiple times in a row, it is followed by (count)
  in parentheses, such as aaa = 1(3).

  It is given that the input string will be correctly formatted.
         
Output: An array of length 26 where index 0 indicates the frequency of letter a as
  an integer, index 1 for letter b, index 25 for letter z, etc.
''' 
def parse_encoded(encoded_string):
    # There may not be any parens in s, but this will make them easier to manage
    sections = encoded_string.split(")")
    freqs = [0] * 26
    for section in sections:
        # Current position (index) in section
        pos = 0
        while pos < len(section):
            # -1 to account for 'a' being at index 0 with an id of 1
            letter_id = int(section[pos]) - 1
            if pos + 2 < len(section) and section[pos + 2] == "#":
                letter_id = int(section[pos:pos+2]) - 1
                # The # sign is the end of this letter, so move there
                pos += 2
            if pos + 1 < len(section) and section[pos + 1] == "(":
                # pos to end of section should be the contents of the parentheses
                freqs[letter_id] += int(section[pos:])
                # Since the section breaks on ")", this is the end of the section,
                #    so break out of the while loop and avoid duplicate additions
                #    of this letter
                break
            pos += 1
            freqs[letter_id] += 1
    return freqs

                
            