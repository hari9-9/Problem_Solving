https://practice.geeksforgeeks.org/problems/squares-in-nn-chessboard/0

def sqr(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    return n*n+sqr(n-1)    

i = int(input())
for k in range(i):
    n= int(input())
    print(sqr(n))
