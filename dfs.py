from tree import Tree
    
def dfs(root, target):
    if root is None:
        return False
    if root.value == target:
        return True
    for child in root.children:
        if dfs(child, target):
            return True
    return False
