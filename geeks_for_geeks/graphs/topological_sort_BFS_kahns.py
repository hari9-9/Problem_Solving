from collections import deque
class Solution:

    #Function to return list containing vertices in Topological order.
    def topologicalSort(self,adj):
        # Code here
        indegree = [0]*len(adj)
        for i in adj:
            for j in i:
                indegree[j]+=1

        q = deque()
        for i in range(len(indegree)):
            if not indegree[i]:
                q.append(i)

        ans = []
        while q:
            curr = q.pop()
            ans.append(curr)
            for nb in adj[curr]:
                indegree[nb]-=1
                if indegree[nb]==0:
                    q.append(nb)
        return ans
