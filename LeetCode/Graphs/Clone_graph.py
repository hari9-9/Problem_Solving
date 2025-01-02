"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:

    def clone(self , node, visited):
        if not node:
            return None
        if node in visited:
            return visited[node]
        c = Node(node.val)
        visited[node] = c
        for n in node.neighbors:
            c.neighbors.append(self.clone(n,visited))
        return c

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = defaultdict(Node)
        return self.clone(node,visited)
        
