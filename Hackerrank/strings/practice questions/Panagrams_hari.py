#!/bin/python3

import math
import os
import random
import re
import sys
CHARS=26
# Complete the pangrams function below.
def pangrams(s):
    s=s.lower()
    print(s)
    score=[0]*CHARS
    i=0
    while i < len(s):
        if(s[i]!=" "):
            score[ord(s[i])-ord('a')] += 1
        i += 1
    print(score)
    if 0 not in score:
        return "pangram"
    else:
        return "not pangram"
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
