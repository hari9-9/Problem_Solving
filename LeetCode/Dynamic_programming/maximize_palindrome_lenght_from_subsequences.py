class Solution:

    def solve(self, s,i,j,dp):
        if i>j:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        if i == j:
            return 1
        ans = 0
        if s[i]==s[j]:
            ans = 2+self.solve(s,i+1,j-1,dp)
        else:
            ans = max(self.solve(s,i+1,j,dp) , self.solve(s,i,j-1,dp))
        dp[i][j] = ans
        return ans

    def longestPalindrome(self, word1: str, word2: str) -> int:
        s = word1 + word2
        n = len(s)
        dp = [[-1 for _ in range(n)] for _ in range(n)]

        # Ensure at least one character from word1 and one from word2 are used
        max_len = 0
        for i in range(len(word1)):
            for j in range(len(word1), len(s)):  # j must belong to word2
                if s[i] == s[j]:  # Possible start of a valid palindrome
                    max_len = max(max_len, 2 + self.solve(s, i + 1, j - 1, dp))

        return max_len
