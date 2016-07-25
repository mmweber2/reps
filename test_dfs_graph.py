from dfs_graph import dfs_graph
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
