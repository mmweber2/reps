class BST(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add_child(self, child):
        if child.value <= self.value:
            if self.left:
                self.left.add_child(child)
            else:
                self.left = child
        else:
            if self.right:
                self.right.add_child(child)
            else:
                self.right = child
