class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        flag = True
        i =0
        res=""
        while flag:
            if i < len(word1):
                res+=word1[i]
            else:
                res+=word2[i:]
                flag = False
                break
            if i < len(word2):
                res+=word2[i]
            else:
                res+=word1[i+1:]
                flag = False
                break
            i+=1
        return res
    
#optimized


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        res=[]
        l1 = len(word1)
        l2 = len(word2)
        while i < l1 and j < l2:
            res.append(word1[i])
            res.append(word2[j])
            i+=1
            j+=1
        res.append(word1[i:])
        res.append(word2[j:])
        return ''.join(res)