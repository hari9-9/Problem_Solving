class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        h={}
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                curr = nums[i]*nums[j]
                h[curr] = h.get(curr,0)+1
        ans = 0
        for key , value in h.items():
            pairs_of_equal_product = (
                (value - 1) * value // 2
            )
            ans += 8*pairs_of_equal_product
        return ans
