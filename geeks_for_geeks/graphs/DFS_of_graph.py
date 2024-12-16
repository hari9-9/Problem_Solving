#User function Template for python3

class Solution:

    def dfs(self, adj,visited,source,ans):
        visited[source] = True
        ans.append(source)
        for i in adj[source]:
            if not visited[i]:
                self.dfs(adj,visited,i,ans)



    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, adj):
        # code here
        visited = [False]* len(adj)
        ans = []
        self.dfs(adj,visited,0,ans)
        return ans
