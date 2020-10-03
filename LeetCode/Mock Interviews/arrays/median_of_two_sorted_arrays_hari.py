class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:    
#         def merge(left, right):
#             a = []
#             i,j=0,0
            
#             nl = len(left)
#             nr = len(right)
            
#             while i<nl and j<nr:
#                 if left[i] <= right[j]:
#                     a.append(left[i])
#                     i+=1
#                 else:
#                     a.append(right[j])
#                     j+=1
                    
#             while i<nl:
#                 a.append(left[i])
#                 i+=1
#             while j<nr:
#                 a.append(right[j])
#                 j+=1
                
#             return a
        
#         lst = merge(nums1, nums2)
        
#         l = len(lst)
#         mid = int(l/2)
        
#         if l%2==0:
#             return((lst[mid-1]+lst[mid])/2)
#         else:
#             return(lst[mid])
        
#         return 0.0     

        s1=len(nums1)
        s2=len(nums2)
        if (s1+s2)%2 !=0:
        
            s3=int(((s1+s2)/2))
            flag=True
        else:
            s3=int(((s1+s2)/2))+1  
            flag=False
        i=0
        j=0
        k=0
        ans=[]
        while(i<=s3 and j<s1 and k<s2):
            if(nums1[j]<nums2[k]):
                ans.append(nums1[j])
                j+=1
            else:
                ans.append(nums2[k])
                k+=1
            i+=1
        while(i<=s3 and j<s1):
            ans.append(nums1[j])
            j+=1
            i+=1
        while(i<=s3 and k<s2):
            ans.append(nums2[k])
            k+=1
            i+=1      
        if(flag):
            return ans[s3]
        else:
            return(float((ans[s3-2]+ans[s3-1]))/2)
        
        
        
