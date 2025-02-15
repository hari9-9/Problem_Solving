class Solution:

    def solve(self,sub,s):
        n = len(s)
        if n %len(sub) != 0:
            return False
        return sub*(n//len(sub)) == s


    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1,len(s)//2 +1):
            sub = s[:i]
            if self.solve(sub,s):
                return True
        return False
