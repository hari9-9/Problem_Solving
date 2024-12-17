#User function Template for python3
from typing import List

class Solution:

    def cycleDFS(self, node,visited,dfsv,adj):
        visited[node] = True
        dfsv[node] = True
        for nb in adj[node]:
            if not visited[nb]:
                det = self.cycleDFS(nb,visited,dfsv,adj)
                if det:
                    return True
            elif dfsv[nb]:
                return True
        dfsv[node] = False
        return False

    #Function to detect cycle in a directed graph.
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        # code here
        visited = [False] * V
        dfsv = [False] * V
        for i in range(V):
            if not visited[i]:
                det = self.cycleDFS(i,visited,dfsv,adj)
                if det:
                    return True
        return False
