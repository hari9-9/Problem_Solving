class Solution:

    def solve(self,capacity,val,wt,i,curr_weight,curr_val,ans):
        if i<len(val):
            # exclude call
            self.solve(capacity,val,wt,i+1,curr_weight,curr_val,ans)

            #include call
            curr_weight+=wt[i]
            curr_value+=val[i]
            if curr_weight<=capacity:
                ans[0] = max(ans[0],curr_val)
                self.solve(capacity,val,wt,i+1,curr_weight,curr_val,ans)



    # Function to return max value that can be put in knapsack of capacity.
    def knapSack(self, capacity, val, wt):
        # code here
        ans = [0]
        curr_weight = 0
        curr_val = 0
        i=0
        self.solve(capacity,val,wt,i,curr_weight,curr_val,ans)
        return ans[0]

class Solution:

    def solve(self , capacity , val , wt, i, curr_weight , dp):
        if i==len(val):
            return 0

        if dp[i][curr_weight] != -1:
            return dp[i][curr_weight]

        exclude = self.solve(capacity , val , wt , i+1 , curr_weight , dp)

        include = 0

        if curr_weight + wt[i] <= capacity:
            include = val[i] + self.solve(capacity , val , wt , i+1 , curr_weight+wt[i] , dp)

        dp[i][curr_weight] = max(include , exclude)

        return dp[i][curr_weight]



    # Function to return max value that can be put in knapsack of capacity.
    def knapSack(self, capacity, val, wt):
        # code here
        dp = [[-1 for _ in range(capacity + 1)] for _ in range(len(val))]

        return self.solve(capacity, val, wt, 0, 0, dp)

# Dp:
