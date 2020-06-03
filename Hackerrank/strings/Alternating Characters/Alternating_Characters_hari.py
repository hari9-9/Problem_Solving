#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    final=[s[0]]
    sum=0
    for alpha in s[1:]:
        if alpha !=final[len(final)-1]:
            final.append(alpha)
        else:
            sum+=1
    return sum




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
