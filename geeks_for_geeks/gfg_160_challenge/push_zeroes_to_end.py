class Solution:
	def pushZerosToEnd(self,arr):
    	# code here
    	curr = 0
    	for i in range(len(arr)):
    	    if arr[i] !=0:
    	        arr[curr] , arr[i] = arr[i] , arr[curr]
    	        curr+=1
    	return arr
