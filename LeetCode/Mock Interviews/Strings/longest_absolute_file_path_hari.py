class Solution:
    def lengthLongestPath(self, input: str) -> int:
        max_len=0
        d={}
        for p in input.split("\n"):
            k=p.count("\t")
            if '.' not in p:
                v=len(p.replace("\t",""))
                d[k]=v
            else:
                temp=k+len(p.replace("\t",""))
                for val in d.keys():
                    if(val<k):
                        temp+=d[val]
                max_len=max(max_len,temp)
        return max_len
