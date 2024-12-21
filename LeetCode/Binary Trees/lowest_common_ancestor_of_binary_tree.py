# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def lca(self, root,n1,n2):
        if not root:
            return None
        if root.val == n1 or root.val ==n2:
            return root
        left = self.lca(root.left,n1,n2)
        right = self.lca(root.right,n1,n2)
        if (left is not None) and (right is not None):
            return root
        elif (left is None) and right:
            return right
        elif(right is None) and left:
            return left
        else:
            return None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = self.lca(root,p.val,q.val)
        return ans