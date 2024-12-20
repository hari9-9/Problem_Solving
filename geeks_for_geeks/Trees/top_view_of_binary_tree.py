#User function Template for python3

# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None

class Solution:
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        # code here
        res = []
        if not root:
            return []
        hash = {}
        q = []
        q.append([root , 0])
        
        while q:
            node , dist = q.pop(0)
            if dist not in hash:
                hash[dist] = node.data
            if node.left:
                q.append([node.left,dist-1])
            if node.right:
                q.append([node.right,dist+1])
        
        for k in sorted(hash.keys()):
            res.append(hash[k])
        return res