class Solution:
    def get_min_max(self, arr):
        small = float('inf')
        big = float('-inf')
        for i in arr:
            small = min(small,i)
            big = max(big,i)
        return [small,big]
