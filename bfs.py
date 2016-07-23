from tree import Tree
    
# Written for a non-binary generic tree
def bfs(tree, target):
    if tree is None:
        return False
    queue = [tree]
    while len(queue) > 0:
        current = queue.pop(0)
        if current.value == target:
            return True
        queue.extend(current.children)
    return False

