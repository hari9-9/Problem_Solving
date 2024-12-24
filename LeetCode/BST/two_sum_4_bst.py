# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inord(self , root, arr):
        if not root:
            return
        self.inord(root.left,arr)
        arr.append(root.val)
        self.inord(root.right, arr)

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        arr = []
        self.inord(root,arr)
        i=0
        j=len(arr)-1
        while(i<j):
            if arr[i]+arr[j] == k:
                return True
            elif arr[i] + arr[j] > k:
                j-=1
            else:
                i+=1
        return False
        
