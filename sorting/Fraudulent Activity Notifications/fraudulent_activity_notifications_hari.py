#!/bin/python3

import math
import os
import random
import re
import sys

def get_median(e):
    e=sorted(e)
    print(e)
    if(len(e)%2==0):
        return(int(((e[int(len(e)/2)])+(e[int(len(e)/2)]))/2))
    else:
        return(e[int(len(e)/2)])


# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    notification=0
    for i in range(len(expenditure)):
        #print(i)
        if i>d:
            print(expenditure[i-d-1:i-1])
            m=get_median(expenditure[i-d-1:i-1])
            print(m,expenditure[i-1])

            if expenditure[i-1]>=2*m:
                notification+=1
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
