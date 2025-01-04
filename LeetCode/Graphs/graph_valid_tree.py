from typing import (
    List,
)

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def dfs(self , edge , adj , visited,prev):
        if edge in visited:
            return False
        visited.add(edge)
        for e in adj[edge]:
            if e != prev:
                if not self.dfs(e,adj,visited,edge):
                    return False
        return True



    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        # write your code here
        adj = {i:[] for i in range(n)}
        for n1 , n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        visited = set()
        dfsval = self.dfs(0,adj,visited,-1)
        return dfsval and len(visited)==n
