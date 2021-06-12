class Solution:
    def frequencySort(self, s: str) -> str:
        val={}
        for ch in s:
            if ch in val:
                val[ch]+=1
            else:
                val[ch]=1
        sort_val = sorted(val.items() , key= lambda x:x[1] , reverse=True)
        ans=[]
        for i in sort_val:
            ans.append(i[0]*i[1])
        return ''.join(ans)
