#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    seq="hackerrank"
    prev=0
    for char in seq:
        print(char)
        if(char in s[prev:]):
            for i in range(prev,len(s)):
                if s[i]==char:
                    prev=i+1
                    print(prev)
                    break
        else:
            return "NO"
    return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
