class Solution:

    def dfs(self,curr,count,visited,rooms):
        if visited[curr]:
            return
        count[0]+=1
        visited[curr]=True
        for n in rooms[curr]:
            self.dfs(n,count,visited,rooms)

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False]*len(rooms)
        count = [0]
        self.dfs(0,count,visited,rooms)
        return count[0] == len(rooms)
        
