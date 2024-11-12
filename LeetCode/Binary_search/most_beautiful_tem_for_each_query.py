class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key = lambda x: x[0])
        max_b = items[0][1]
        for i in range(len(items)):
            max_b = max(max_b , items[i][1])
            items[i][1] = max_b
        return [self.binary_search(items,q) for q in queries]

    def binary_search(self, items, target_price):
        l , r = 0 , len(items)-1
        max_b = 0
        while l <= r:
            mid = (l+r)//2
            if items[mid][0] > target_price:
                r = mid -1
            else:
                max_b = max(max_b , items[mid][1])
                l = mid +1
        return max_b
