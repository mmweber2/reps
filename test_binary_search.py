from binary_search import bsearchr
from binary_search import bsearchi
from nose.tools import assert_equals

def test_empty_lists():
    assert_equals(bsearchi([], 0), -1)
    assert_equals(bsearchr([], 0), -1)

def test_single_item_present():
    li = [0]
    assert_equals(bsearchi(li, 0), 0)
    assert_equals(bsearchr(li, 0), 0)

def test_single_item_absent():
    li = [0]
    assert_equals(bsearchi(li, 1), -1)
    assert_equals(bsearchr(li, 1), -1)

def test_two_items_sorted_present():
    li = [0, 5]
    assert_equals(bsearchi(li, 0), 0)
    assert_equals(bsearchr(li, 0), 0)

def test_two_items_sorted_absent():
    li = [0, 5]
    assert_equals(bsearchi(li, 10), -1)
    assert_equals(bsearchr(li, 10), -1)

def test_three_items_sorted_present():
    li = [0, 1, 5]
    assert_equals(bsearchi(li, 1), 1)
    assert_equals(bsearchr(li, 1), 1)