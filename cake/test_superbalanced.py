from superbalanced import BinaryTreeNode
from superbalanced import is_superbalanced as f
#from nose.tools import assert_equals

# No tests included for the BinaryTreeNode class itself,
#   as it came from the problem statement.
def test_empty_tree():
    assert f([])

def test_single_node():
    a = BinaryTreeNode("1")
    assert f(a)

