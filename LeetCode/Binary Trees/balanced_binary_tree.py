# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root):
        if not root:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        ans = max(left,right)+1
        return ans
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)
        diff = abs(self.height(root.left)-self.height(root.right)) <=1
        return left and right and diff

        
