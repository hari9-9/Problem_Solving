# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # def height(self, root):
    #     if not root:
    #         return 0
    #     left = self.height(root.left)
    #     right = self.height(root.right)
    #     ans = max(left,right)+1
    #     return ans

    # def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
    #     op1 = self.diameterOfBinaryTree(root.left)
    #     op2 =  self.diameterOfBinaryTree(root.right)
    #     op3 = self.height(root.left) + self.height(root.right)
    #     return max(op1,max(op2,op3))
    def diafast(self, root):
        if not root:
            return (0,0)
        left = self.diafast(root.left)
        right = self.diafast(root.right)
        opt1 = left[0]
        opt2 = right[0]
        opt3 = left[1]+right[1]
        return (max(opt1,max(opt2,opt3)) ,max(left[1],right[1])+1 )



    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.diafast(root)[0]
