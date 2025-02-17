class Solution:

    def solve(self,data):
        ans = 0
        for tile , count in data.items():
            if count > 0:
                ans +=1
                data[tile] -= 1
                ans +=self.solve(data)
                data[tile] += 1
        return ans

    def numTilePossibilities(self, tiles: str) -> int:
        data = {}
        for i in tiles:
            data[i] = data.get(i,0)+1
        print(data)
        return self.solve(data)
