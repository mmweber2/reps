from nose.tools import assert_equals
from parse_encoded import parse_encoded

def get_base_array():
    return [0] * 26

def test_single_char():
    arr = get_base_array()
    arr[0] = 1
    assert_equals(parse_encoded("1"), arr)

def test_two_digit_char():
    arr = get_base_array()
    arr[25] = 1
    assert_equals(parse_encoded("26#"), arr)

def test_single_digit_multiple_occurrence():
    arr = get_base_array()
    arr[0] = 2
    arr[1] = 1
    assert_equals(parse_encoded("121"), arr)

def test_two_digit_multiple_occurrence():
    arr = get_base_array()
    arr[0] = 1
    arr[25] = 2
    assert_equals(parse_encoded("26#126#"), arr)