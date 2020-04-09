#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    up=0
    lo=0
    sym=0
    dig=0
    count=0
    for char in password:
        if char.isalpha():
            if char.isupper():
                up+=1
            else:
                lo+=1
        elif char.isdigit():
            dig+=1
        else:
            sym+=1
    if up<1:
        count+=1
    if lo<1:
        count+=1
    if sym<1:
        count+=1
    if dig<1:
        count+=1
    if(n+count)<6:
        count+=6-(n+count)
    return count

    # Return the minimum number of characters to make the password strong

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
