# naive two pass

class Solution:
    def reverseVowels(self, s: str) -> str:
        
        def isVowel(a):
            return a.lower() in ['a','e','i','o','u']
    
        vlist = []
        for c in s:
            if isVowel(c):
                vlist.append(c)
        if len(vlist)==0:
            return s
        i=0
        vlist = vlist[::-1]
        res = ''
        for c in s:
            if isVowel(c):
                res += vlist[i]
                i+=1
            else:
                res+=c
        return res


        
# Two pointer approach :

class Solution:
    def reverseVowels(self, s: str) -> str:
        
        def isVowel(a):
            return a.lower() in ['a','e','i','o','u']
    
        l=0
        r= len(s)-1
        s=list(s)
        while l<r:
            if not isVowel(s[l]) and not isVowel(s[r]):
                l+=1
                r-=1
            elif not isVowel(s[l]):
                l+=1
            elif not isVowel(s[r]):
                r-=1
            else:
                s[l] , s[r] = s[r] , s[l]
                l+=1
                r-=1
        return ''.join(s)


# Two pointers with simplified ifs
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        s = list(s)
        left, right = 0, len(s)-1

        while right > left:
            leftS = s[left].lower()
            rightS = s[right].lower()
            if leftS not in vowels:
                left += 1
                continue
            if rightS not in vowels:
                right -= 1
                continue
            s[left], s[right] = s[right], s[left]
            left, right = left+1, right-1
        return ''.join(s)


# Two pointers ifs optimized with while to beat 94% of runtime

class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels = 'aeiouAEIOU'
        
        s = list(s)
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and s[l] not in vowels:
                l+=1
            while l < r and s[r] not in vowels:
                r-=1
            s[l], s[r] = s[r], s[l]
            l+=1
            r-=1
        return "".join(s)