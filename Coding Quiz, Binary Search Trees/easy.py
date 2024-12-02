'''
Easy: (3 points)

1. Write a Python function to insert a value into a binary search tree. 
The function should take the root of the tree and the value to be inserted as parameters.
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if not root:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root
