# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def solve(self , root, depth , ans):
        if not root:
            return
        if not root.left and not root.right:
            ans[0] = min(ans[0] , depth)
            return
        self.solve(root.left , depth+1 , ans)
        self.solve(root.right , depth+1 , ans)


    def minDepth(self, root: Optional[TreeNode]) -> int:
        ans = [float("inf")]
        self.solve(root ,1 , ans)
        if ans[0] == float("inf"):
            return 0
        return ans[0]
