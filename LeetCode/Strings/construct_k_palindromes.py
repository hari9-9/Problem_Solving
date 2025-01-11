class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s)<k:
            return False
        if len(s)==k:
            return True

        arr = [0]*26
        for c in s:
            arr[ord(c)-ord('a')]+=1
        odd=0
        for c in arr:
            if c%2 ==1:
                odd +=1
        return odd<=k
