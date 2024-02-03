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
        
