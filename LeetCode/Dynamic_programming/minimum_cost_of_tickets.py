class Solution:

    def solve(self,days,costs,ind,dp):
        if ind >= len(days):
            return 0
        if dp[ind] !=-1:
            return dp[ind]
        op1 = costs[0] + self.solve(days,costs,ind+1,dp)

        i=ind
        while(i<len(days) and days[i]<days[ind]+7):
            i+=1
        op2 = costs[1] + self.solve(days,costs,i,dp)

        i=ind
        while(i<len(days) and days[i]<days[ind]+30):
            i+=1
        op3 = costs[2] + self.solve(days,costs,i,dp)
        dp[ind] = min(op1,min(op2,op3))
        return dp[ind]


    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [-1]*len(days)
        return self.solve(days,costs,0,dp)
