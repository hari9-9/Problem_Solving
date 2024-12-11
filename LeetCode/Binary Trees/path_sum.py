# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    @staticmethod
    def summer(root,target,curr):
        if root:
            curr+=root.val
            if root.left == None and root.right== None:
                if curr==target:
                    return True
                else:
                    return False

            return Solution.summer(root.left,target,curr) or Solution.summer(root.right,target,curr)
        else:
            return False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return Solution.summer(root,targetSum,0)
