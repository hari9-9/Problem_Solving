class Solution:

    def expand(self , s , i , j,ans,res):
        while i <= j and 0<=i<len(s) and 0<=j<len(s):
            if s[i]==s[j]:
                i-=1
                j+=1
            else:
                break
        if j-i-1 > ans[0]:
            res[0] = "".join(s[i+1 : j])
            ans[0] = j-i-1

    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        s= list(s)
        ans = [1]
        res = [s[0]]
        for i in range(len(s)):
            self.expand(s,i,i,ans,res)
            self.expand(s,i,i+1,ans,res)
        return res[0]
