from is_connected import is_connected
from nose.tools import assert_equals
# Given a list of edges in an undirected graph, determine
# whether all points are connected.
def test_empty_list():
    assert_equals(is_connected([]), True)

def test_self_loop():
    assert_equals(is_connected([[1, 1]]), True)

def test_two_points():
    assert_equals(is_connected([[1, 2]]), True)

def test_chain_end_connected():
    assert_equals(is_connected([[1, 2], [3, 4], [2, 4]]), True)

def test_chain_front_connected():
    assert_equals(is_connected([[1, 2], [3, 4], [1, 3]]), True)

def test_chain_front_to_end_connected():
    assert_equals(is_connected([[1, 2], [3, 4], [1, 4]]), True)

def test_two_disjoint():
    assert_equals(is_connected([[1, 2], [3, 4]]), False)

def test_three_two_disjoint():
    assert_equals(is_connected([[1, 2], [3, 4], [1, 6]]), False)

def test_forked():
    assert_equals(is_connected([[1, 2], [1, 3], [3, 4]]), True)

def test_long_chain():
    input_list = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
    assert_equals(is_connected(input_list), True)
