# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0  # Initialize the global variable
    def summer(self,root,curr):
            curr*=10
            curr= curr+root.val
            if (not root.left) and (not root.right):
                self.ans+=curr
                return
            if root.left:
                self.summer(root.left,curr)
            if root.right:
                self.summer(root.right,curr)
            return
        

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.ans = 0
        self.summer(root,0)
        return self.ans
        