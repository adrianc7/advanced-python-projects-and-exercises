'''
Medium: (5 points)

2. Implement a Python function to search for a value in a binary search tree.
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def search(root, val):
    if not root:
        return False
    if root.val == val:
        return True
    if val < root.val:
        return search(root.left, val)
    return search(root.right, val)
