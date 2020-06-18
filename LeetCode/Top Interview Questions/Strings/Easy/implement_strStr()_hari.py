class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #print(len(haystack),len(needle))
        l=len(needle)
        k=len(haystack)
        if l == 0:
            return 0
        i=0
        while(i<=(k-l)):
            print(haystack[i:i+l])
            if(needle == haystack[i:i+l] ):
                return i
            i+=1
            
        return(-1)
