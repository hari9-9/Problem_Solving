class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        def dfs(x,y,i) -> bool:
            if len(word)-1 ==i:
                return word[i]==board[x][y]
            if board[x][y] != word[i]:
                return False
            temp = board[x][y]
            board[x][y] = "0"
            directions = [(-1,0),(0,1),(1,0),(0,-1)]
            for dx , dy in directions:
                nx = x+dx
                ny = y+dy
                if 0<=nx<rows and 0<=ny<cols and board[nx][ny]!=0:
                    if dfs(nx,ny,i+1):
                        return True
            board[x][y] = temp
            return False

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0] and dfs(i,j,0):
                    return True
        return False
