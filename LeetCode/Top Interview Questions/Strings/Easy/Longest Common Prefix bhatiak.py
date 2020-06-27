class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if strs == []:
            return ""

        l=len(strs[0])
        for i in range(1, len(strs)):
            if len(strs[i]) < l:
                l=len(strs[i])
        
        ans = []
        for i in range(l):
            flag=True
            t = strs[0][i]
            for str in strs:
                if str[i] != t:
                    flag=False
                    break
                elif str[i] == t:
                    continue
            
            if flag==False:
                return "".join(ans)
            if flag==True:
                ans.append(t)
                    
        return "".join(ans)
