class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def combi(nums,ans,curr,size):
            if(len(curr)==size):
                ans.append(curr)
                return
            #print(nums,ans,curr,size)
            for i in range(len(nums)):
                c=curr.copy()
                n=nums.copy()
                c.append(n[i])
                n.remove(n[i])
                combi(n,ans,c,size)
        
        
        ans=[]
        curr=[]
        combi(nums,ans,curr,len(nums))
        return ans
