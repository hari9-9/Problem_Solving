class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        col = len(matrix[0])
        while row < len(matrix) and not (matrix[row][0]<=target<=matrix[row][col-1]):
            row+=1
        if row ==len(matrix):
            return False
        left = 0
        right = col
        while(left<=right):
            mid = (left+right)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid-1
            else:
                left = mid+1
        return False
