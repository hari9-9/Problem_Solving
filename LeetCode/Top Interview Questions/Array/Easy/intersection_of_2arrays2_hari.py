 class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = {}
        d = {}

        for i in nums1:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
            d[(i, count[i])] = 1
        #print(d)
        #print(count)
        count = {}
        for i in nums2:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
            if (i, count[i]) in d:
                d[(i, count[i])] += 1
        #print(d)
        vals = []
        for key in d:
            #print(vals)
            if d[key] > 1:
                vals.append(key[0])

        return vals



class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash1={}
        hash2={}
        for i in nums1:
            if i in hash1:
                hash1[i]+=1
            else:
                hash1[i]=1
        for i in nums2:
            if i in hash2:
                hash2[i]+=1
            else:
                hash2[i]=1
        res = []
        for i in hash1:
            if i in hash2:
                v=min(hash1[i],hash2[i])
                while v:
                    res.append(i)
                    v-=1
        return res
