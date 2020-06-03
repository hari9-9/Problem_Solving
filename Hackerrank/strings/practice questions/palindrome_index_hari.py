#!/bin/python3

import math
import os
import random
import re
import sys
def isPalindrome(string: str, low: int, high: int): 
    while low < high: 
        if string[low] != string[high]: 
            return False
        low += 1
        high -= 1
    return True
def palindromeIndex(string):
    low = 0
    high = len(string) - 1
    while low < high: 
        if string[low] == string[high]: 
            low += 1
            high -= 1
        else: 
            if isPalindrome(string, low + 1, high): 
                return low 
            if isPalindrome(string, low, high - 1): 
                return high 
            return -1
    return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
