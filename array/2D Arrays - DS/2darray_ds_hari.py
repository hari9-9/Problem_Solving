#!/bin/python3
#https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&isFullScreen=false&playlist_slugs%5B%5D%5B%5D%5B%5D%5B%5D%5B%5D%5B%5D%5B%5D%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D%5B%5D%5B%5D%5B%5D%5B%5D%5B%5D%5B%5D%5B%5D=arrays
import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    i=0
    j=0
    m=-100
    while(i<6):
        while(j<6):
            if(i+2)<6 and (j+2)<6:
                s=arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
                if(s>m):
                    m=s
            j=j+1
        i=i+1
        j=0
    return m
            


        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
