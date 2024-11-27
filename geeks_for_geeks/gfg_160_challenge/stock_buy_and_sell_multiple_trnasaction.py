from typing import List


class Solution:
    def maximumProfit(self, prices) -> int:
        # code here
        n = len(prices)
        b = prices[0]
        s = prices[0]
        i=0
        p=0
        while i<n-1:
            while i<n-1 and prices[i]>=prices[i+1]:
                i+=1
            b = prices[i]
            while i <n-1 and prices[i]<=prices[i+1]:
                i+=1
            s = prices[i]
            p+=s-b
        return p



#{
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        solution = Solution()
        res = solution.maximumProfit(arr)
        print(res)

# } Driver Code Ends
