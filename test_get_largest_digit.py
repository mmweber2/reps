from get_largest_digit import get_largest_digit
from nose.tools import assert_equals

def test_minimum_size():
    assert_equals(get_largest_digit(1, 1), 2)

def test_multiple_digit_sum():
    assert_equals(get_largest_digit(5, 5), 1)

def test_same_digit_sum():
    assert_equals(get_largest_digit(5, 6), 1)

def test_all_digits():
    assert_equals(get_largest_digit(123456788, 1), 9)

def test_large_numbers():
    assert_equals(get_largest_digit(2**32, 2**32), 9)
    