# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @staticmethod
    def preorder(root,ans):
        if root:
            Solution.preorder(root.left,ans)
            Solution.preorder(root.right,ans)
            ans.append(root.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        Solution.preorder(root,ans)
        return ans
