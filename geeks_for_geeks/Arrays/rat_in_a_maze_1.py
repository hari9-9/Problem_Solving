# #User function Template for python3
class Solution:
    # Function to find all possible paths
    def findPath(self, mat):
        # code here
        rows = len(mat)
        cols = len(mat[0])
        directions = [(-1, 0, 'U'), (0, 1, 'R'), (1, 0, 'D'), (0, -1, 'L')]
        def dfs(mat,ans,path,i,j):
            #base case
            if i==rows-1 and j==cols-1:
                ans.append("".join(path))
                return
            for dx , dy, move in directions:
                nx = i+dx
                ny = j+dy
                if 0<=nx<rows and 0<=ny<cols and mat[nx][ny] == 1:
                    mat[nx][ny] = 0
                    path.append(move)
                    dfs(mat,ans,path,nx,ny)
                    path.pop()
                    mat[nx][ny] = 1


        ans = []
        path = []
        mat[0][0] = 0
        dfs(mat,ans,path,0,0)
        return sorted(ans)
