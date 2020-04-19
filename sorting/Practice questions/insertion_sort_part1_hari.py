#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    e=arr[len(arr)-1]
    #print(e)
    flag=0
    i=len(arr)-2
    #print(arr[i])
    while i>=0:
        if(arr[i]>=e):
            arr[i+1]=arr[i]
            if i==0:
                flag=1
        else:
            arr[i+1]=e
            print(*arr, sep = " ") 
            break

        print(*arr, sep = " ") 
        i-=1
    if flag==1:
        arr[0]=e
        print(*arr, sep = " ") 




if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
