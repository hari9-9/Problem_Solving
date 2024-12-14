# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans
        dq = []
        dq.append(root)
        while dq:
            ans.append(dq[-1].val)
            for _ in range(len(dq)):
                curr = dq.pop(0)
                if curr.left:
                    dq.append(curr.left)
                if curr.right:
                    dq.append(curr.right)
        return ans
        
