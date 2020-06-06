class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l = len(nums)
        k= k-l*(int(k/l))
        for i in range(k):
            nums.insert(0, nums.pop())
