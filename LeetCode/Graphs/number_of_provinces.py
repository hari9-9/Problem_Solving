class Solution:

    def dfs(self,city,isConnected,visited):
        visited[city] = True
        neighbours = isConnected[city]
        for i in range(len(neighbours)):
            if not visited[i] and neighbours[i]:
                self.dfs(i,isConnected,visited)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False]*len(isConnected)
        ans = 0
        for city in range(len(isConnected)):
            if not visited[city]:
                self.dfs(city,isConnected,visited)
                ans+=1
        return ans
