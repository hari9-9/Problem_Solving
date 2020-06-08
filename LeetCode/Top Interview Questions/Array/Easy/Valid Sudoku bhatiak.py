"""
this is my original solution:
Runtime: 148 ms
Memory Usage: 14 MB
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check the rows
        if(len(board[0]) == 3):
            temp = []
        for i in range(0,len(board[0])):
            if len(board[0]) != 3:
                temp = []
            for j in range(0,len(board[0])):
                if board[i][j] in temp:
                    return False
                else:
                    if board[i][j] is not '.':
                        temp.append(board[i][j])
            
        # Check the columns
        if(len(board[0]) == 3):
            temp = []
        for i in range(0,len(board[0])):
            if len(board[0]) != 3:
                temp = []
            for j in range(0,len(board[0])):
                if board[j][i] in temp:
                    return False
                else:
                    if board[j][i] is not '.':
                        temp.append(board[j][i])
                
        boxes = []
        if(len(board[0]) > 3):
            for a in range(0, len(board[0]), 3):
                for b in range(0, len(board[0]), 3):
                    mini_board = []
                    for i in range(a, a+3):
                        temp = []
                        for j in range(b, b+3):
                            temp.append(board[i][j])
                        mini_board.append(temp)
                    # print(mini_board)
                    boxes.append(self.isValidSudoku(mini_board))
        
        for case in boxes:
            if case==False:
                return False
        return True
