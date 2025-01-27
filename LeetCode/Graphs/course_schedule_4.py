class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for pre , crs in prerequisites:
            adj[crs].append(pre)

        def dfs(crs):
            if crs not in reqMap:
                reqMap[crs] = set()
                for pre in adj[crs]:
                    reqMap[crs] |= dfs(pre)
                reqMap[crs].add(crs)
            return reqMap[crs]

        reqMap = {}
        for crs in range(numCourses):
            dfs(crs)
        res = []
        for u,v in queries:
            res.append(u in reqMap[v])
        return res
        
