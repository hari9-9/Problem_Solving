class Solution:

    def dfs(self,i,graph,safe):
        if i in safe:
            return safe[i]
        safe[i] = False
        for n in graph[i]:
            if not self.dfs(n,graph,safe):
                return safe[i]
        safe[i] = True
        return True

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe = {}
        ans = []
        for i in range(len(graph)):
            if self.dfs(i,graph,safe):
                ans.append(i)
        return ans        
