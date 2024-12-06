class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_set = set()
        col_set = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    row_set.add(i)
                    col_set.add(j)
        print(row_set)
        print(col_set)
        for row in row_set:
            for j in range(len(matrix[row])):
                matrix[row][j] = 0
        for row in range(len(matrix)):
            for col in col_set:
                matrix[row][col] = 0
        
        
        
