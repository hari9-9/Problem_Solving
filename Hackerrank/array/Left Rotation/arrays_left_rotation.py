#!/bin/python3
#https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    # if len(a) == d:
    #     return a

    # temp=0
    no_of_rots =  int(d % len(a))

    # for i in range(no_of_rots):
    #     temp = a[0]
    #     a = a[1:]
    #     a.append(temp)

    temp = a[0:no_of_rots]
    a = a[no_of_rots:]
    a += temp

    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
