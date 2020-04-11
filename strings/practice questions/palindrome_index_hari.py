#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the palindromeIndex function below.
def palindromeIndex(s):
    pal=s
    if s==s[::-1]:
        return(-1)
    for i in range(len(s)):
        pal=s[:i]+s[i+1:]
        if(pal==pal[::-1]):
            return(i)
    return(-1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
