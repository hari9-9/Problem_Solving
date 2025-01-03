# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q=[]
        ans = []
        q.append(root)
        lvl =0
        while q:
            ln = len(q)
            curr_n = float('-inf')
            for _ in range(ln):
                node = q.pop(0)
                curr_n = max(curr_n,node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(curr_n)
            lvl+=1
        return ans
        
