class Solution:

    def solve(self, s, wordDict, index, dp):
        # Base case: If we reach the end of the string, return True
        if index == len(s):
            return True

        # If already computed, return the cached result
        if dp[index] != -1:
            return dp[index]

        # Try to match every possible prefix starting from `index`
        for word in wordDict:
            # Check if the word fits in the substring and matches
            if s[index:index + len(word)] == word:
                # Recur for the remaining part of the string
                if self.solve(s, wordDict, index + len(word), dp):
                    dp[index] = True
                    return True

        # If no segmentation works, store and return False
        dp[index] = False
        return dp[index]

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Initialize memoization array with -1
        dp = [-1] * len(s)
        # Start solving from the beginning of the string
        return self.solve(s, wordDict, 0, dp)



class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[len(s)] = True
        for i in range(len(s)-1 , -1,-1):
            for w in wordDict:
                if (i+len(w)<=len(s) and s[i:i+len(w)]==w):
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break
        return dp[0]
