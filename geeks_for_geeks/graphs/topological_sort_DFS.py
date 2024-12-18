class Solution:

    def topSort(self,node,adj,visited,stack):
        visited[node] = True
        for nb in adj[node]:
            if not visited[nb]:
                self.topSort(nb,adj,visited,stack)
        stack.append(node)
    #Function to return list containing vertices in Topological order.
    def topologicalSort(self,adj):
        # Code here
        visited = [False]*len(adj)
        stack = []
        for i in range(len(adj)):
            if not visited[i]:
                self.topSort(i,adj,visited,stack)

        stack.reverse()
        return stack
