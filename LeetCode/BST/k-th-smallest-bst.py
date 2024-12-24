# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:

#     def solve(self,root,ans,k):
#         if not root:
#             return
#         self.solve(root.left,ans,k)
#         ans.append(root.val)
#         if len(ans)==k or len(ans)>k:
#             return
#         self.solve(root.right,ans,k)

#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         ans = []
#         self.solve(root,ans,k)
#         return ans[k-1]

class Solution:

    def solve(self,root,i,k):
        if not root:
            return -1
        left = self.solve(root.left,i,k)
        if left!=-1:
            return left
        i[0]+=1
        if i[0]==k:
            return root.val
        return self.solve(root.right,i,k)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        i = [0]
        ans = self.solve(root,i,k)
        return ans
