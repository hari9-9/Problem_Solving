class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        hash = {}
        res = []
        for i in arr:
            hash[i] = hash.get(i,0)+1

        for i in hash.keys():
            if hash[i] > len(arr)//3:
                res.append(i)
        res.sort()
        return res
