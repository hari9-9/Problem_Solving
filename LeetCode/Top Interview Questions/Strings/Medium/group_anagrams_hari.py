class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        primes=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]
        ret = {}
        for s in strs:
            ans=1
            for c in s:
                ans*=primes[ord(c)-97]
            if(ans not in ret):
                ret[ans]=[]
            ret[ans].append(s)
        res=[]
        #print(ret)
        for s in ret:
            res.append(ret[s])
        return res
