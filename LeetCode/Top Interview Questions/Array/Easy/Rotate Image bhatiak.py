"""
this is my original solution.
Runtime: 40 ms
Memory Usage: 13.7 MB
"""

class Solution:
    
    def transpose(self, x):
        i=0
        while(i<len(x)):
            j=i
            while(j<len(x[i])):
                x[i][j], x[j][i] = x[j][i], x[i][j]
                j+=1
            i+=1

    def swapcols(self, x):
        l=len(x)
        i=0
        while i<len(x):
            j=0
            while j<int(len(x[0])/2):
                x[i][j], x[i][l-j-1] = x[i][l-j-1], x[i][j]
                j+=1
            i+=1
            
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.swapcols(matrix)
