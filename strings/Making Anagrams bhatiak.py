#!/bin/python3

import math
import os
import random
import re
import sys

def makeAnagram(a, b, i):
    return 0 if i==-1 else abs(a.count(chr(97+i)) - b.count(chr(97+i))) + makeAnagram(a, b, i-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    a = input()
    b = input()
    res = makeAnagram(a, b, 26)
    fptr.write(str(res) + '\n')
    fptr.close()
