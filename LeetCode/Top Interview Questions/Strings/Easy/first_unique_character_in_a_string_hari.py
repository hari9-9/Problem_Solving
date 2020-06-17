class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        #print(count)
        
        # find the index
        for idx, ch in enumerate(s):
            #print(idx,ch)
            if count[ch] == 1:
                return idx     
        return -1
