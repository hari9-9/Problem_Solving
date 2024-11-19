class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l = 0
        hmap = {}
        c_sum = 0
        res = 0

        for r in range(len(nums)):
            c_sum += nums[r]
            hmap[nums[r]] = hmap.get(nums[r], 0) + 1

            if r - l + 1 > k:
                c_sum -= nums[l]
                hmap[nums[l]] -= 1
                if hmap[nums[l]] == 0:
                    hmap.pop(nums[l])
                l += 1


            if r - l + 1 == k and len(hmap) == k:
                res = max(res, c_sum)

        return res
