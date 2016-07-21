from components import connected_components as comp
from nose.tools import assert_equals

# Given a list of edges in an undirected graph, determine how many
# connected components there are.

def test_empty():
    assert_equals(comp([]), 0)

def test_self_loop():
    assert_equals(comp([[1, 1]]), 1)

def test_two_points():
    assert_equals(comp([[1, 2]]), 1)

def test_chain_end_connected():
    assert_equals(comp([[1, 2], [3, 4], [2, 4]]), 1)

def test_chain_front_connected():
    assert_equals(comp([[1, 2], [3, 4], [1, 3]]), 1)

def test_chain_front_to_end_connected():
    assert_equals(comp([[1, 2], [3, 4], [1, 4]]), 1)

def test_two_disjoint():
    assert_equals(comp([[1, 2], [3, 4]]), 2)

def test_three_two_disjoint():
    assert_equals(comp([[1, 2], [3, 4], [1, 6]]), 2)

def test_forked():
    assert_equals(comp([[1, 2], [1, 3], [3, 4]]), 1)

def test_long_chain():
    input_list = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
    assert_equals(comp(input_list), 1)

def test_three_components():
    input_list = [[1, 2], [7, 8], [3, 2], [4, 5], [5, 6]]
    assert_equals(comp(input_list), 3)


