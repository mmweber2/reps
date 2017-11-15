def get_largest_digit(a, b):
    return max(int(digit) for digit in str(a + b))

'''
Version without max:
def get_largest_digit(a, b): 
    largest_digit = 0
    for digit in str(a + b):
        if int(digit) > largest_digit:
            largest_digit = int(digit)
    return largest_digit
'''

# Notes:
# If not in Python, a + b could overflow.
# What should the return type be? int?
# In Python, "9" > "8", but this isn't a given for other languages.
# a + b are given to be positive, so their sum cannot be 0.

# Write a function that takes two positive integers as parameters, adds them, and returns the largest digit of the sum.