# Interview Cake problem "Balanced Binary Tree"
# BinaryTreeNode class copied from problem statement.
class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

def is_superbalanced(root):
    if not root:
        return True
    leaf_heights = []
    # Nodes and their heights
    stack = [(root, 0)]
    while stack:
        node, depth = stack.pop()
        if not (node.right or node.left):
            # Node is a leaf
            if depth not in leaf_heights:
                # Using a set would allow us to skip this step,
                #  but would make it harder to compare the height difference
                leaf_heights.append(depth)
            if (len(leaf_heights) > 2 or
                    (len(leaf_heights) == 2 and
                     leaf_heights[1] > leaf_heights[0] + 1)):
                return False
        else:
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
    return True
