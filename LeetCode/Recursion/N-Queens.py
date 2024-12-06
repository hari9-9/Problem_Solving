class Solution:
    @staticmethod
    def addBoard(ans,board):
        ans.append([''.join(row) for row in board.copy()])

    @staticmethod
    def isSafe(row,col,board,n):
        x = row
        y = col
        while y>=0:
            if board[x][y]=='Q':
                return False
            y-=1
        x= row
        y = col
        while x>=0 and y>=0:
            if board[x][y] == 'Q':
                return False
            y-=1
            x-=1
        x = row
        y = col
        while x<n and y>=0:
            if board[x][y] == 'Q':
                return False
            y-=1
            x+=1
        return True


    @staticmethod
    def solve(col,ans, board,n):
        if col == n:
            Solution.addBoard(ans,board)
            return
        for row in range(len(board)):
            if Solution.isSafe(row,col,board,n):
                board[row][col] = 'Q'
                Solution.solve(col+1,ans,board,n)
                board[row][col] = '.'



    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        ans = []
        Solution.solve(0,ans,board,n)
        return ans

        
