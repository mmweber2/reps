def dfs(tree, target):
    if tree is None:
        return False
    if tree.value == target:
        return True
    if tree.value < target:
        return dfs(tree.left, target)
    return dfs(tree.right, target)
