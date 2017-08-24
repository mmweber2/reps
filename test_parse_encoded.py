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

def test_multiple_count_single_digit():
    arr = get_base_array()
    arr[0] = 2
    assert_equals(parse_encoded("1(2)"), arr)

def test_multiple_count_double_digit():
    arr = get_base_array()
    arr[12] = 2
    assert_equals(parse_encoded("13#(2)"), arr)

def test_multiple_parens():
    arr = get_base_array()
    arr[6] = 5
    arr[2] = 2
    assert_equals(parse_encoded("3(2)7(5)"), arr)

def test_complex():
    arr = get_base_array()
    arr[0] = 1
    arr[1] = 1
    arr[25] = 1
    arr[23] = 3
    assert_equals(parse_encoded("1226#24#(3)"), arr)
