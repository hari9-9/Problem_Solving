class Solution:
    def minSteps(self, s: str, t: str) -> int:
        h1 = {}
        for i in t:
            h1[i] = h1.get(i,0)+1

        for i in s:
            if i in h1:
                h1[i]= h1.get(i,0)-1
                if h1[i]<0:
                    del h1[i]
        ans = 0
        for key , val in h1.items():
            ans+=val
        return ans





# class Solution:
#     def minSteps(self, s: str, t: str) -> int:
#         h1 = {}
#         h2 = {}
#         for i in s:
#             h1[i] = h1.get(i,0)+1
#         for i in t:
#             h2[i] = h2.get(i,0)+1
#         ans = 0
#         for key , value in h2.items():
#             if key in h1:
#                 if h1[key]>value:
#                     ans+=h1[key]-value
#             else:
#                 ans+=h
#         return ans
        
