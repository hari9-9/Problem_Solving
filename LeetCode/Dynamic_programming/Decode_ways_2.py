class Solution:
    def solve(self, s, i, dp):
        MOD = 10**9 + 7

        if i == len(s):
            return 1
        if i in dp:
            return dp[i]
        if s[i] == "0":  # A leading '0' is not valid
            return 0

        ans = 0

        # Case 1: Single character decoding
        if s[i] == "*":
            ans = 9 * self.solve(s, i + 1, dp)  # '*' can be '1' to '9'
        else:
            ans = self.solve(s, i + 1, dp)

        # Case 2: Two-character decoding
        if i + 1 < len(s):
            if s[i] == "1":
                if s[i + 1] == "*":
                    ans += 9 * self.solve(s, i + 2, dp)  # "1*" can be "11" to "19"
                else:
                    ans += self.solve(s, i + 2, dp)  # "1X" where X is 0-9
            elif s[i] == "2":
                if s[i + 1] == "*":
                    ans += 6 * self.solve(s, i + 2, dp)  # "2*" can be "21" to "26"
                else:
                    if "0" <= s[i + 1] <= "6":
                        ans += self.solve(s, i + 2, dp)  # "2X" where X is 0-6
            elif s[i] == "*":
                if s[i + 1] == "*":
                    ans += 15 * self.solve(s, i + 2, dp)  # "**" can be "11-19" + "21-26" = 15 possibilities
                elif "0" <= s[i + 1] <= "6":
                    ans += 2 * self.solve(s, i + 2, dp)  # "*X" where X is 0-6 → 1X or 2X
                else:
                    ans += self.solve(s, i + 2, dp)  # "*X" where X is 7-9 → only 1X is valid

        dp[i] = ans % MOD  # Store result with modulo
        return dp[i]

    def numDecodings(self, s: str) -> int:
        dp = {}
        return self.solve(s, 0, dp)
