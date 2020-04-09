#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    subs=[]
    for i in range(n+1):
        for j in range(n-i+1):
            subs.append(s[j:j+i])
    subs=subs[n+1:]
    print(subs)
    final=[]
    for sub in subs:
        char_dict={}
        for char in sub:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
        #print(len(char_dict))
        if(len(char_dict)==2 and sub==sub[::-1]):
            final.append(sub)
        elif(len(char_dict)==1):
            final.append(sub)
        else:
            None

    return(len(final))



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
