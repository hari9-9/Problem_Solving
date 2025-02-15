class Solution:

    def _checker(self,target,num):
        if not num and target == 0:
            return True
        if target<0:
            return False
        for i in range(len(num)):
            l = num[:i+1]
            r = num[i+1:]
            lnum = int(l)
            if self._checker(target-lnum,r):
                return True
        return False

    def punishmentNumber(self, n: int) -> int:
        ans = 0
        for num in range(1,n+1):
            if self._checker(num,str(num * num)):
                ans+=num*num
        return ans

            
