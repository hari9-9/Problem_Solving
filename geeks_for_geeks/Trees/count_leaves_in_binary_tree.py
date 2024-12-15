'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function
# function should return the count of Leaf node's
# Note: You required to print a new line after every test case
class Solution:

    def counter(self,root):
        if not root:
            return 0
        if root.left== None and root.right == None:
            return 1
        return self.counter(root.left) + self.counter(root.right)

    # Function to count the number of leaf nodes in a binary tree.
    def countLeaves(self, root):
       return self.counter(root)
