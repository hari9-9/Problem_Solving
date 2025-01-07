class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        ans = 0
        q= []
        q.append((entrance[0],entrance[1]))
        maze[entrance[0]][entrance[1]] = '+'
        while q:
            ans+=1
            for _ in range(len(q)):
                x , y, = q.pop(0)
                dirs = [[0,1],[1,0],[-1,0],[0,-1]]
                for dx , dy in dirs:
                    curx = dx+x
                    cury = dy+y
                    if 0<=curx<len(maze) and 0<=cury<len(maze[0]) and maze[curx][cury]=='.':
                        if curx == 0 or curx==len(maze)-1 or cury == 0 or cury ==len(maze[0])-1:
                            return ans
                        q.append((curx,cury))
                        maze[curx][cury] = '+'
        return -1

        
