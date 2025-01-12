class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}
        for crs , pre in prerequisites:
            graph[crs].append(pre)
        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if graph[crs] == []:
                return True
            visited.add(crs)
            for pre in graph[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            graph[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True



### graph coloring:
class Solution:

    def color(self,graph,visited,i):
        if visited[i]==2:
            return True
        visited[i] = 2
        for n in graph[i]:
            if visited[n] !=1:
                if self.color(graph,visited,n):
                    return True
        visited[i] = 1
        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [0]*numCourses
        graph = {i:[] for i in range(numCourses)}

        for crs , pre in prerequisites:
            graph[crs].append(pre)

        for i in range(numCourses):
            if visited[i]==0:
                if self.color(graph,visited,i):
                    return False
        return True
