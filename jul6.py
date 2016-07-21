class BST(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Note: Does not balance
    def add_child(self, new_value):
        # Allows duplicate values, follows convention that they fit on the
        # left side
        if new_value <= self.value:
            if self.left is None:
                # If we wanted add_child to take a BST instead of a value, we
                # could create child once and pass it to all of these methods.
                self.left = BST(new_value)
            else:
                self.left.add_child(new_value)
        else:
            if self.right is None:
                self.right = BST(new_value)
            else:
                self.right.add_child(new_value)
