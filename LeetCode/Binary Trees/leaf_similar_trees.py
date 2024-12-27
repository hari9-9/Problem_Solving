# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def getLeafs(self,root,t):
        if not root:
            return
        self.getLeafs(root.left,t)
        if not root.left and not root.right:
            t.append(root.val)
            return
        self.getLeafs(root.right,t)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        t1 = []
        t2 = []
        self.getLeafs(root1,t1)
        self.getLeafs(root2,t2)
        print(t1)
        print(t2)
        return t1==t2
