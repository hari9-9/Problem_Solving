class Solution:
    @staticmethod
    def nextChar(c):
        return 'a' if c =='z' else chr(ord(c)+1)

    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i=0
        j=0
        while i <len(str1) and j < len(str2):
            if str1[i] == str2[j] or Solution.nextChar(str1[i])== str2[j]:
                i+=1
                j+=1
            else:
                i+=1
        return j==len(str2)
