#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    largest = -100
    temp = 0

    r = len(arr)
    c = len(arr[0])

    for i, vali in enumerate(arr):
        for j, valj in enumerate(vali):
            if i+2<r and j+2<c:
                temp = arr[i][j] + arr[i][j+1] + arr[i][j+2]
                temp += arr[i+1][j+1]
                temp += arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]

                if temp > largest:
                    largest = temp
    return largest

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
