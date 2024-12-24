# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def preOrd(self,root,pre):
        if not root:
            return
        pre.append(root)
        self.preOrd(root.left,pre)
        self.preOrd(root.right, pre)

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        pre = []
        self.preOrd(root,pre)
        for i in range(len(pre)-1):
            curr= pre[i]
            curr.right = pre[i+1]
            curr.left = None
        pre[-1].right = None
        pre[-1].left = None
        
