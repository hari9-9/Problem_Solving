#!/bin/python3

import math
import os
import random
import re
import sys

def insertionSort2(ar):
    for i in range(1, len(ar)):
        temp = ar[i]
        j = i
        while j > 0 and temp < ar[j-1]:
            ar[j] = ar[j-1]
            j -= 1
        ar[j] = temp
        print(*arr, sep = " ") 



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(arr)
