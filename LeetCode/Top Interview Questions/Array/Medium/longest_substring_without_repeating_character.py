class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = set()
        ans = 0
        curr =0
        i=0
        j=0
        while j< len(s):
            if s[j] not in hash:
                hash.add(s[j])
                j+=1
                ans = max(len(hash),ans)
            else:
                hash.remove(s[i])
                i+=1
        return max(len(hash),ans)
