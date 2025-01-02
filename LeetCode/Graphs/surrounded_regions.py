class Solution:

    def dfs(self,r,c,board):
        if (r<0 or c<0 or r==len(board) or c==len(board[0]) or board[r][c]!='O'):
            return
        board[r][c] = 'T'
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        for dr , dc in dirs:
            self.dfs(r+dr , c+dc , board)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        for r in range(len(board)):
            for c in range(len(board[0])):
                if (board[r][c] == 'O' and (r in [0,rows-1] or c in [0,cols-1])):
                    self.dfs(r,c,board)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'T':
                    board[r][c] = 'O'



        
