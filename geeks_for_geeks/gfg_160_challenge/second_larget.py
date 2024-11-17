#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        l = 0
        for i in arr:
            l = max(i,l)
        l2 = 0
        for i in arr:
            if i != l:
                l2 = max(i,l2)
        if l2:
            return l2
        else:
            return -1
