class Solution:
    def bottomView(self, root):
        # code here
        res = []
        if not root:
            return []
        hash = {}
        q = []
        q.append([root , 0])
        
        while q:
            node , dist = q.pop(0)
            hash[dist] = node.data
            if node.left:
                q.append([node.left,dist-1])
            if node.right:
                q.append([node.right,dist+1])
        
        for k in sorted(hash.keys()):
            res.append(hash[k])
        return res