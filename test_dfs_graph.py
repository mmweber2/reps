from dfs_graph import dfs_graph
from dfs_graph import has_cycle

# dfs_graph_tests
def test_empty_list():
    assert not dfs_graph([], 1, 'A')

def test_start_not_in_graph():
    assert not dfs_graph([[1, 1]], 2, 1)

def test_start_cycle_target():
    assert dfs_graph([[1, 1]], 1, 1)

def test_start_cycle_not_target():
    assert not dfs_graph([[1, 1]], 1, 2)

def test_second_point():
    assert dfs_graph([[1, 2]], 1, 2)

def test_chain_end_connected():
    assert dfs_graph([[1, 2], [3, 4], [2, 4]], 1, 3)

def test_chain_front_connected():
    assert dfs_graph([[1, 2], [3, 4], [1, 3]], 1, 4)

def test_chain_front_to_end_connected():
    assert dfs_graph([[1, 2], [3, 4], [1, 4]], 1, 3)

def test_cycle_later_in_graph():
    assert dfs_graph([[1, 2], [3, 4], [5, 6], [5, 1], [6, 7]], 1, 7)

def test_in_graph_unreachable():
    assert not dfs_graph([[1, 2], [3, 4]], 1, 3)

def test_forked():
    assert dfs_graph([[1, 2], [1, 3], [3, 4]], 1, 4)

def test_long_chain():
    input_list = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
    assert dfs_graph(input_list, 1, 6)

# has_cycle tests
def test_has_cycle_empty():
    assert not has_cycle([])

def test_has_cycle_single_edge():
    assert not has_cycle([[1, 2]])

def test_has_cycle_self_loop():
    assert has_cycle([[1, 1]])

def test_has_cycle_two_points():
    assert has_cycle([[1, 2], [2, 1]])

def test_has_cycle_three_points():
    assert has_cycle([[1, 2], [2, 3], [3, 1]])

def test_has_cycle_not_beginning():
    assert has_cycle([[1, 2], [2, 3], [3, 2]])



