# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = []
        q.append([root,0,0])
        node = defaultdict(list)
        while q:
            curr, height, dist = q.pop(0)
            node[dist].append([height,curr.val])
            if curr.left:
                q.append([curr.left , height+1 , dist-1])
            if curr.right:
                q.append([curr.right,height+1,dist+1])
        sorted_col = sorted(node.keys())
        res = []
        for col in sorted_col:
            column_nodes = sorted(node[col], key=lambda x: [x[0], x[1]])
            res.append([val for row, val in column_nodes])
        return res