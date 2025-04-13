# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def solve(self , root, res):
        if not root:
            return 0
        left = max(self.solve(root.left, res) , 0)
        right = max(self.solve(root.right,res),0)
        res[0] = max(res[0] , root.val + left + right)
        return max(root.val +left , root.val + right)



    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = [root.val]
        self.solve(root , res)
        return res[0]