class Solution:
    def solve(self,s,wordDict,i,curr,ans):
        if i ==len(s):
            ans.append(" ".join(curr))
            return
        for word in wordDict:
            if s[i:i+len(word)] == word:
                curr.append(word)
                self.solve(s,wordDict,i+len(word),curr,ans)
                curr.pop()
        return

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        self.solve(s,wordDict,0,[],ans)
        return ans
