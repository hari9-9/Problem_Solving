#User function Template for python3

class Solution:

    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr):
        #Your code here
        arr.sort()
        i=1
        curr = 0
        while(curr<len(arr)):
            if arr[curr] <=0:
                curr+=1
            else:
                break
        while(curr<len(arr)):
            if arr[curr]!=i:
                return i
            else:
                while curr < len(arr) and arr[curr]==i:
                    curr+=1
                i+=1
        return i
