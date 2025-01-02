class Solution:

    def dfs(self ,r,c,visited,heights):
        if (r,c) in visited:
            return
        visited.add((r,c))
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        for dr , dc in dirs:
            rt = r+dr
            ct = c+dc
            if 0<=rt<len(heights) and 0<=ct<len(heights[0]) and heights[rt][ct] >=heights[r][c]:
                self.dfs(rt,ct,visited,heights)

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        for i in range(len(heights)):
            self.dfs(i,0,pacific,heights)
            self.dfs(i,len(heights[0])-1, atlantic,heights)

        for i in range(len(heights[0])):
            self.dfs(0,i,pacific,heights)
            self.dfs(len(heights)-1,i, atlantic,heights)
        ans = []
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if (r,c) in pacific and (r,c) in atlantic:
                    ans.append([r,c])
        return ans


        
