class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if(len(str1)>len(str2)):
            s1=list(str1)
            s2=list(str2)
        else:
            s1=list(str2)
            s2=list(str1)
        if(s1[0]!=s2[0]):
            return ""
        flag=False
        ref=s2.copy()
        while(len(ref)):
            print(len(s1),len(s2),len(s1)%len(s2))
            if(len(s1)%len(ref)==0 and len(s2)%len(ref)==0):
                for i in range(len(s1)):
                    if(s1[i]!=ref[i%len(ref)]):
                        ref.pop()
                        continue
                for i in range(len(s2)):
                    if(s2[i]!=ref[i%len(ref)]):
                        ref.pop()
                        continue
                return "".join(ref)
            else:
                ref.pop()
                
        return ""
