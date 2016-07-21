def bfs(tree, target):
    if tree.value == target:
        return tree
    queue = tree.edges
    while len(queue) > 0:
        node = queue.pop(0)
        if node.value == target: return True
        queue.extend(node.edges)
    return False

def dfs(tree, target):
    if tree == None:
        return False
    if tree.value == target:
        return True
    results = [dfs(x, target) for x in tree.children]
    return any(results)
