#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):
    count=[0]*100
    for i in arr:
        count[i]+=1
    sort_arr=[]
    for i in range(len(count)):
        v=count[i]
        #print(v)
        while(v>0):
            sort_arr.append(i)
            print("added",i)
            v-=1
    return sort_arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
