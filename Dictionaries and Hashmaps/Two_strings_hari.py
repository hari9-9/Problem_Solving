#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    subs_1=[]
    subs_2=[]
    for i in range(len(s1)):
        for j in range(i,len(s1)):
            #print(s1[i:j+1])
            subs_1.append(s1[i:j+1])
    for i in range(len(s2)):
        for j in range(i,len(s2)):
            #print(s2[i:j+1])
            subs_2.append(s2[i:j+1])
    a_set = set(subs_1) 
    b_set = set(subs_2) 
    if (a_set & b_set): 
        return "YES" 
    else: 
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
