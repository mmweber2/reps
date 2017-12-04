# Hackerrank problem Maximum Gcd and Sum
# https://www.hackerrank.com/contests/w34/challenges/maximum-gcd-and-sum/problem
 
# Adapted from editorial solution.
 
# Note: A and B are converted to sets before passing to this function.
def maximumGcdAndSum(A, B):
    limit = 10**6 + 1 # Per problem statement
    largest_mults_a = {}
    largest_mults_b = {}
    for factor in xrange(1, limit):
        for multiple in xrange(factor, limit, factor):
            if multiple in A:
                largest_mults_a[factor] = multiple
            if multiple in B:
                largest_mults_b[factor] = multiple
    for multiple in xrange(limit - 1, 0, -1):
        if multiple in largest_mults_a and multiple in largest_mults_b:
            return largest_mults_a[multiple] + largest_mults_b[multiple]



