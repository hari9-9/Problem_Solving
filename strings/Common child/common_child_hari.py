#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the commonChild function below.
def commonChild(s1, s2):
    x = len(s1)
    y = len(s2)
    n = [[0 for _ in range(y+1)] for _ in range(x+1)]
    for i in range(1,x+1):
        for j in range(1,y+1):
            if s1[i-1]==s2[j-1]:
                n[i][j]=1+n[i-1][j-1]
            else:
                n[i][j] =max(n[i-1][j],n[i][j-1])
    return n[x][y] 



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
