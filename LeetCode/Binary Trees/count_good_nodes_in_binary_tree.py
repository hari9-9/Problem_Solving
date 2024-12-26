# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,root,val,ans):
        if not root:
            return
        if root.val >=val:
            ans[0]+=1
        val = max(val,root.val)
        self.solve(root.right,val,ans)
        self.solve(root.left,val,ans)

    def goodNodes(self, root: TreeNode) -> int:
        ans = [0]
        val = float('-inf')
        self.solve(root,val,ans)
        return ans[0]

        
