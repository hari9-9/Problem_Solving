class Solution:
    
    def leftTraversal(self,root,level,ans):
        if not root:
            return
        if level == len(ans):
            ans.append(root.data)
        self.leftTraversal(root.left,level+1,ans)
        self.leftTraversal(root.right,level+1,ans)
    
    def LeftView(self, root):
        # code here
        ans = []
        self.leftTraversal(root,0,ans)
        return ans