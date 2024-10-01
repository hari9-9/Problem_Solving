class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        rem = {}
        for i in arr:
            val = (i%k + k)%k
            if val in rem:
                rem[val]+=1
            else:
                rem[val]=1
        for i in arr:
            val = (i%k + k)%k
            if val == 0:
                if rem[val] % 2 == 1:
                    return False
            elif rem[val] != rem.get(k-val,0):
                return False
        return True