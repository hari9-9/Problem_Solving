class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc = []
        max_inc = 1
        max_dec = 1
        dec = []
        if not nums:
            return 0
        if len(nums)==1:
            return 1
        inc.append(nums[0])
        dec.append(nums[0])
        for i in range(1,len(nums)):
            if inc[-1]<nums[i]:
                inc.append(nums[i])
                max_inc = max(max_inc , len(inc))
            else:
                inc = []
                inc.append(nums[i])

            if dec[-1]>nums[i]:
                dec.append(nums[i])
                max_dec = max(max_dec , len(dec))
            else:
                dec = []
                dec.append(nums[i])
        return max(max_inc , max_dec)




class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Initialize the lengths of the increasing and decreasing subarrays
        inc_len = 1  # A subarray of size 1 is trivially increasing
        dec_len = 1  # A subarray of size 1 is trivially decreasing
        max_len = 1  # Maximum length of the monotonic subarrays

        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                # If strictly increasing
                inc_len += 1
                dec_len = 1  # Reset decreasing length
            elif nums[i] < nums[i - 1]:
                # If strictly decreasing
                dec_len += 1
                inc_len = 1  # Reset increasing length
            else:
                # If neither increasing nor decreasing (equal elements)
                inc_len = 1
                dec_len = 1

            # Update the maximum length encountered so far
            max_len = max(max_len, inc_len, dec_len)

        return max_len
