from typing import List
from collections import deque
class Solution:

    def cycleBFS(self,adj,visited,source):
        parent = {}
        q = deque()
        q.append(source)
        visited[source] = True
        parent[source] = -1
        while q:
            curr = q.popleft()
            for i in adj[curr]:
                if visited[i] and parent[curr]!=i:
                    return True
                elif not visited[i]:
                    visited[i] = True
                    q.append(i)
                    parent[i] = curr
        return False



    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
        visited = [False]*V
        for i in range(V):
            if not visited[i]:
                ans = self.cycleBFS(adj,visited,i)
                if ans:
                    return True
        return False
