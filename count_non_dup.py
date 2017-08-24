# Based on a HackerRank problem.
# Start and end can each be up to 10**6.
# TODO: Solution for multiple ranges at once
def count_special(start, end):
    '''Returns the number of special integers between start and end.
    
    Given two integers start and end, return the number of special integers between
    start and end (inclusive). A number is said to be special if it has no duplicate numbers.
    For example, 12 is special, but 11 and 121 are not.

    It is given that start and end are valid integers and start <= end.

    Returns:
        An integer count of the special numbers in the given range.
    '''
    #print [x for x in range(start, end + 1) if len(set(str(x))) != len(str(x))]
    return len([x for x in range(start, end + 1) if len(set(str(x))) == len(str(x))])
    