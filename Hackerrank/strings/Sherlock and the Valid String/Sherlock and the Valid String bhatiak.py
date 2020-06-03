#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    result = 0
    letters = []
    for letter in s:
         letters.append(letter) if letter not in letters else None

    a = letters[0]
    for letter in letters[1:]:
        temp = abs(s.count(a) - s.count(letter))
        result += temp if temp <= 1 else 1 if s.count(letter) == 1 else temp
    
    return 'NO' if result > 1 else 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = isValid(s)
    fptr.write(result + '\n')
    fptr.close()
