class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        str1 , str2 = [] , []
        str1[:0] = s
        str2[:0] = t
        len1 , len2 = len(str1) , len(str2)
        i , j =0 , 0
        while i< len1 and j<len2:
            if str1[i] == str2[j]:
                j+=1
                i+=1
            else:
                j+=1
        
        if i==len1:
            return True
        else:
            return False
        


# optimization
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        i , j =0 , 0
        while i< len(s) and j<len(t):
            if s[i] == t[j]:
                i+=1
            j+=1
        return i==len(s)