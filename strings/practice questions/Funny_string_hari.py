#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    srev=s[::-1]
    print(srev)
    sc=[]
    rc=[]
    for i in range(len(s)):
        sc.append(ord(s[i]))
        rc.append(ord(srev[i]))
    flag=0
    for i in range(len(s)-1):
        if(abs(sc[i]-sc[i+1])!=abs(rc[i]-rc[i+1])):
            flag=1
    if flag==0:
        return("Funny")
    else:
        return("Not Funny")




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
