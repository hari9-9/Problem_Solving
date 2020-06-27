class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(strs == [] or "" in strs):
            return ''
        m = len(strs[0])
        ind = 0
        l=0
        for i in range(1,len(strs)):
            if(len(strs[i])<m):
                m = len(strs[i])
                ind = i
        #print(m,ind)
        for i in range(m):
            c= strs[0][i]
            for j in strs:
                if(j[i]!=c):
                    return(strs[0][:i])
                
        return strs[ind]
