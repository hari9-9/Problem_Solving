# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def inord(self,root,t):
        if not root:
            return
        self.inord(root.left,t)
        t.append(root.val)
        self.inord(root.right,t)

    def bal(self,s,e,t):
        if s >e:
            return None
        mid = (s+e)//2
        root = TreeNode(val = t[mid])
        root.left = self.bal(s,mid-1,t)
        root.right = self.bal(mid+1,e,t)
        return root


    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        t = []
        self.inord(root,t)
        root = self.bal(0,len(t)-1,t)
        return root
        
