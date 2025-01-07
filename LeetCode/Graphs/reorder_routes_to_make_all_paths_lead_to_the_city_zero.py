class Solution:

    def dfs(self , city, edges,neigh,visited,ans):
        for node in neigh[city]:
            if node in visited:
                continue
            if (node,city) not in edges:
                ans[0]+=1
            visited.add(node)
            self.dfs(node,edges,neigh,visited,ans)



    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = {(a,b) for a,b in connections}
        neigh = {i:[] for i in range(n)}
        for a,b in connections:
            neigh[a].append(b)
            neigh[b].append(a)
        visited = set()
        visited.add(0)
        ans = [0]
        self.dfs(0,edges,neigh,visited,ans)
        return ans[0]
