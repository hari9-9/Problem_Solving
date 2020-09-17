class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        q=[]
        for i in range(len(S)):
            if(S[i]!='-'):
                if(S[i].isupper()):
                    q.append(S[i])
                else:
                    q.append(S[i].upper())
        l=len(q)
        rem=l%K
        ans=[]
        for i in range(rem):
            ans.append(q[i])
        if(len(ans)>0):
            c=K
        else:
            c=0
        for i in range(rem,len(q)):
            if(c==K):
                ans.append('-')
                c=0
            c+=1
            ans.append(q[i])
        #print(ans)
        return ''.join(ans)
