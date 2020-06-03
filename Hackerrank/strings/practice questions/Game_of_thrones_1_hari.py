#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gameOfThrones function below.
def gameOfThrones(s):
    char_dict={}
    for aplha in s:
        if aplha in char_dict:
            char_dict[aplha] += 1
        else:
            char_dict[aplha] = 1
    #print(char_dict)
    flag=0
    for n in char_dict.values():
        #print(n)
        if n%2!=0:
            flag+=1
            #print(flag)
    if(flag==0 or flag==1):
        return("YES")
    else:
        return("NO")


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
