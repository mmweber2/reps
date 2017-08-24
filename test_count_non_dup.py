from count_non_dup import count_special
from nose.tools import assert_equals

def test_single_number_special():
    assert_equals(count_special(10, 10), 1)

def test_single_number_not_special():
    assert_equals(count_special(11, 11), 0)

def test_two_digit_range_all_special():
    assert_equals(count_special(12, 21), 10)
    
def test_range_non_special_ends():
    assert_equals(count_special(11, 22), 10)

def test_range_two_three_digit_special_ends():
    # Answer from brute force solution
    assert_equals(count_special(102, 203), 74)

def test_range_two_three_digit_non_special_ends():
    # Answer from brute force solution
    assert_equals(count_special(101, 331), 168)

