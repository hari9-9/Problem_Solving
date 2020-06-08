class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[]
        for i in range(9):
            row = board[i][:]
            #print(row)
            for elem in row:
                if elem is not ".":
                    #print(row.count(elem))
                    if row.count(elem) > 1:
                        return False
                    
        for i in range(9):
            col=[]
            for j in range(9):
                col.append(board[j][i])
            #print(col)
            for elem in col:
                if elem is not ".":
                    #print(row.count(elem))
                    if col.count(elem) > 1:
                        return False
        l1 = [0,1,2]
        l2 = [0,1,2]
        for k in range(9):
            box=[]
            for i in l1:
                for j in l2:
                    box.append(board[i][j])
            print(box)
            for elem in box:
                if elem is not ".":
                    #print(row.count(elem))
                    if box.count(elem) > 1:
                        return False
            
            l1 = [x+3 for x in l1]
            if(9 in l1):
                l1=[0,1,2]
                l2 = [x+3 for x in l2]
                    
            
        
        return True
