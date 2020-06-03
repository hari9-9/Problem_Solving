#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickSort function below.
def quickSort(arr):
    p=arr[0]
    l=[]
    r=[]
    e=[]
    for i in arr:
        if(i>p):
            r.append(i)
        elif(i<p):
            l.append(i)
        else:
            e.append(i)
    l.extend(e)
    l.extend(r)
    return(l)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
