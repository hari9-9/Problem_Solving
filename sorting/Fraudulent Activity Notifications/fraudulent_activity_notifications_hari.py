#!/bin/python3
#intrestin algo reffer https://jjromi.github.io/2017/lucky_45/
import math
import os
import random
import re
import sys

def get_median(count,d):
    s=0
    for i in range(len(count)):
        s+=count[i]
        if((2*s)==d):
            return((2*i+1))
        elif((2*s)>d):
            return(2*i)
    return(1)


# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    count=[0]*201
    notification=0
    for i in range(d):
        count[expenditure[i]]+=1
    for i in range(d,len(expenditure)):
        m=get_median(count,d)
        if m<=expenditure[i]:
            notification+=1 
        count[expenditure[i-d]]-=1
        count[expenditure[i]]+=1
    return notification  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()

