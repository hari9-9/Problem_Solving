class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        hash = {}
        for c in s:
            hash[c] = hash.get(c,0)+1
        heap = []
        for k,v in hash.items():
            heap.append((-ord(k),v))
        heapq.heapify(heap)

        ans = []
        while heap:
            negated_char , count = heapq.heappop(heap)
            char = chr(-negated_char)
            use = min(repeatLimit , count)
            ans.append(char * use)
            if count > use and heap:
                next_negated_char , next_count  = heapq.heappop(heap)
                ans.append(chr(-next_negated_char))
                if next_count > 1:
                    heapq.heappush(heap,(next_negated_char,next_count-1))
                heapq.heappush(heap,(negated_char,count-use))
        return "".join(ans)
