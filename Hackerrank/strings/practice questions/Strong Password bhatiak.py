#!/bin/python3

import math
import os
import random
import re
import sys

def count_chars(s):
    ualpha = 0
    lalpha = 0
    num = 0
    sym = 0
    for char in s:
        if char.isalpha():
            if char.islower():
                lalpha += 1
            elif char.isupper():
                ualpha += 1
        elif char.isdigit():
            num += 1
        else:
            sym += 1
    return "%d %d %d %d" % (ualpha, lalpha, num, sym)

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    count = 0
    ualpha, lalpha, num, sym = map(int, count_chars(password).split())

    if ualpha < 1:
        count += 1
    if lalpha < 1:
        count += 1
    if num < 1:
        count += 1
    if sym < 1:
        count += 1

    if (n+count)<6:
        count += 6-(n+count)
        
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
