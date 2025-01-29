class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            left = i
            right = i
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
                ans+=1
            left =i
            right = i+1
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
                ans+=1
        return ans
