class Solution:

    def inorder(self,root,v):
        if not root:
            return None
        self.inorder(root.left,v)
        v.append(root.data)
        self.inorder(root.right,v)

    def merge(self, root1, root2):
        # code here
        i1=[]
        self.inorder(root1,i1)
        i2 = []
        self.inorder(root2,i2)
        ans = []
        i=0
        j=0
        while(i<len(i1) and j<len(i2)):
            if i1[i]<=i2[j]:
                ans.append(i1[i])
                i+=1
            else:
                ans.append(i2[j])
                j+=1

        while(i<len(i1)):
            ans.append(i1[i])
            i+=1
        while(j<len(i2)):
            ans.append(i2[j])
            j+=1

        return ans
