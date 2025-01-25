# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def inord(self,root,hash):
        if not root:
            return
        self.inord(root.left,hash)
        hash[root.val] = hash.get(root.val,0)+1
        self.inord(root.right,hash)

    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        hash = {}
        self.inord(root,hash)
        max_freq = 0
        for key , value in hash.items():
            max_freq = max(max_freq,value)
        ans = []
        for key , value in hash.items():
            if value==max_freq:
                ans.append(key)
        return ans
