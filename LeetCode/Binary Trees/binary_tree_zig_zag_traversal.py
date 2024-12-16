# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        q = []
        q.append(root)
        flag = True
        while q:
            s = len(q)
            temp = []
            for i in range(s):
                front = q.pop(0)
                temp.append(front.val)
                if front.left:
                    q.append(front.left)
                if front.right:
                    q.append(front.right)
            if flag:
                ans.append(temp)
            else:
                ans.append(temp[::-1])
            flag = not flag
        return ans
