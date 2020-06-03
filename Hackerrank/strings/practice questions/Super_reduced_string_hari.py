#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    final=[s[0]]
    for alpha in s[1:]:
        if len(final)==0:
            final.append(alpha)
        elif alpha !=final[len(final)-1]:
            final.append(alpha)
        else:
            del final[-1]
    if len(final)==0:
        return("Empty String")
    else:
        result=""
        re=result.join(final)
        return(re)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
