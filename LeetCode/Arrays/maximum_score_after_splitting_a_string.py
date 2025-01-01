class Solution:
    def maxScore(self, s: str) -> int:
        left = []
        curr = 0
        for i in range(len(s)):
            v = int(s[i])
            if v == 0:
                curr+=1
            left.append(curr)
        right = []
        curr = 0
        for i in range(len(s)-1,-1,-1):
            v = int(s[i])
            if v == 1:
                curr+=1
            right.insert(0,curr)
        ans = 0
        for i in range(1,len(left)):
            ans = max(ans,left[i-1]+right[i])
        return ans

        
