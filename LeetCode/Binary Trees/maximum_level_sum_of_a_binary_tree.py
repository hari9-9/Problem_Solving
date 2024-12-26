# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        lvl=1
        q=[]
        q.append(root)
        ans = float('-inf')
        level = 0
        while q:
            ln = len(q)
            curr = 0
            for _ in range(ln):
                node = q.pop(0)
                curr+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if curr > ans:
                ans = curr
                level = lvl
            lvl+=1
        return level

        
