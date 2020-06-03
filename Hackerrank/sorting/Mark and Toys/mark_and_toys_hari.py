#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices.sort()
    w=0
    num=0
    while(w<=k):
        prices.sort()
        if(prices[0]>k-w):
            return num
        for i in prices:
            if (i+w)<=k:
                w=w+i
                num+=1
                prices.remove(i)
                #print(prices)
                break
    return num

            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
