#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    score=0
    if n>=6:
        result=4
        for alpha in password:
            if(alpha in numbers):
                score+=1
        if score>0:
            result-=1
        score=0
        for alpha in password:
            if(alpha in lower_case):
                score+=1
        if score>0:
            result-=1
        score=0
        for alpha in password:
            if(alpha in upper_case):
                score+=1
        if score>0:
            result-=1
        score=0
        for alpha in password:
            if(alpha in special_characters):
                score+=1
        if score>0:
            result-=1
        score=0
        return(result)
    else:
        return(6-n)
    # Return the minimum number of characters to make the password strong

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
