class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls = {}
        hash = {}
        ans = []
        for ball , color in queries:
            if ball in balls:
                temp = balls[ball]
                if hash[temp] ==1:
                    del hash[temp]
                else:
                    hash[temp]-=1
            hash[color] = hash.get(color,0)+1
            balls[ball] = color
            ans.append(len(hash.keys()))
        return ans
