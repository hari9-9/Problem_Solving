# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        q=[]
        q.append(root)
        lvl = 0
        while q:
            ln = len(q)
            curr_nodes = []
            for _ in range(ln):
                node = q.pop(0)
                curr_nodes.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if lvl % 2 == 1:
                left, right = 0, len(curr_nodes) - 1
                while left < right:
                    tmp = curr_nodes[left].val
                    curr_nodes[left].val = curr_nodes[right].val
                    curr_nodes[right].val = tmp
                    left += 1
                    right -= 1
            lvl+=1
        return root

        