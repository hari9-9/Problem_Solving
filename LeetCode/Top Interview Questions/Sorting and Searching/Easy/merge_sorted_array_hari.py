class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        init_len = len(nums1)
        n1=nums1[0:m]
        nums1[:]=[]
        i=0
        j=0
        while i<m and j<n :
            if(n1[i]<=nums2[j]):
                nums1.append(n1[i])
                i+=1
            else:
                nums1.append(nums2[j])
                j+=1
        if(i<m):
            nums1.extend(n1[i:])
    
        if(j<n):
            nums1.extend(nums2[j:])
        while(len(nums1)<init_len):
            nums1.append(0)

        
        
        """
        Do not return anything, modify nums1 in-place instead.
        """
