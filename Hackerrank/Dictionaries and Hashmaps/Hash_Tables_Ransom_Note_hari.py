#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    words={}
    for word in magazine:
        if word in words.keys():
            words[word]+=1
        else:
            words[word]=1
    #print(words)
    for word in note:
        if word in words.keys() and words[word]!=0:
            words[word]-=1
        else:
            print("No")
            return
    print("Yes")
    return



    

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
