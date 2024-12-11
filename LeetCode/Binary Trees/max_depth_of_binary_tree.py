# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans=0

    def preorder(self,root,depth):
        if root:
            self.ans = max(depth,self.ans)
            self.preorder(root.left,depth+1)
            self.preorder(root.right,depth+1)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.preorder(root,1)
        return self.ans
