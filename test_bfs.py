from bfs import bfs
from bfs import Tree
import mock
from nose.tools import assert_equals
def test_empty():
    assert not bfs(None, 3)

def test_single_item():
    root = Tree(6)
    assert bfs(root, 6)

def test_single_child():
    root = Tree(6)
    root.add_child(Tree(2))
    assert bfs(root, 2)

def test_non_first_child():
    root = Tree(6)
    root.add_child(Tree(2))
    root.add_child(Tree(1))
    assert bfs(root, 1)

def test_not_in_tree():
    root = Tree(6)
    root.add_child(Tree(2))
    assert not bfs(root, 1)

# Add two children to the root, then another child to the first of the
# root's children. Is the second root-child searched before the root's
# grandchild?
def test_traversal():
    root = Tree(1)
    first_child = Tree(2)
    root.add_child(first_child)
    first_child.add_child(Tree(4))
    root.add_child(Tree(3))
    # Traversal order verified with print statements, since the function is
    # only called once (no recursion).
    assert bfs(root, 3)
