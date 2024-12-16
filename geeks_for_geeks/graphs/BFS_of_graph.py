from typing import List
from collections import deque
#User function Template for python3
class Solution:
    # Function to return Breadth First Traversal of given graph.

    def bfs(self,adj: List[List[int]],node,ans):
        q = deque()
        visited = [False]* len(adj)
        visited[node] = True
        q.append(node)

        while q:
            curr = q.popleft()
            ans.append(curr)
            for x in adj[curr]:
                if not visited[x]:
                    q.append(x)
                    visited[x] = True


    def bfsOfGraph(self, adj: List[List[int]]) -> List[int]:
        # code here
        ans = []
        self.bfs(adj,0,ans)
        return ans
