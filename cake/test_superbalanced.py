from superbalanced import BinaryTreeNode
from superbalanced import is_superbalanced as f
#from nose.tools import assert_equals

# No tests included for the BinaryTreeNode class itself,
#   as it came from the problem statement.

# The values aren't being examined at all, so we should be able to
#   test with the same values every time.
def test_empty_tree():
    assert f([])

def test_single_node():
    a = BinaryTreeNode(1)
    assert f(a)

def test_single_leaf():
    a = BinaryTreeNode(1)
    a.insert_left(2)
    assert f(a)

def test_two_leaves_diff_zero():
    a = BinaryTreeNode(1)
    a.insert_left(2)
    a.insert_right(2)
    assert f(a)

def test_two_leaves_diff_one_left():
    a = BinaryTreeNode(1)
    b = a.insert_left(2)
    b.insert_left(2)
    assert f(a)

def test_two_leaves_diff_one_right():
    a = BinaryTreeNode(1)
    b = a.insert_left(2)
    b.insert_right(2)
    assert f(a)

def test_left_only():
    # This tree is not balanced in the normal sense, but it meets
    #   the definition of superbalanced.
    a = BinaryTreeNode(1)
    b = a.insert_left(2)
    b.insert_left(2)
    assert f(a)

def test_right_only():
    a = BinaryTreeNode(1)
    b = a.insert_right(2)
    b.insert_right(2)
    assert f(a)

def test_unbalanced_two_heights():
    a = BinaryTreeNode(1)
    # Two children in root's right subtree
    a.insert_right(2).insert_left(3)
    # Root's left subtree
    b = a.insert_left(2)
    b.insert_left(3)
    d = b.insert_right(4)
    d.insert_left(5).insert_left(6)
    assert not f(a)

def test_unbalanced_3_heights():
    a = BinaryTreeNode(1)
    a.insert_right(2)
    b = a.insert_left(2)
    b.insert_left(3).insert_left(4)
    b.insert_right(4)
    assert not f(a)



