# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def solve(self,root,k,path,count):
        if not root:
            return
        path.append(root.val)
        self.solve(root.left,k,path,count)
        self.solve(root.right,k,path,count)

        s = len(path)
        sum = 0
        for i in range(s-1,-1,-1):
            sum+=path[i]
            if sum==k:
                count[0]+=1
        path.pop()


    def pathSum(self, root: Optional[TreeNode], k: int) -> int:
        path = []
        count = [0]
        self.solve(root,k,path,count)
        return count[0]
        
