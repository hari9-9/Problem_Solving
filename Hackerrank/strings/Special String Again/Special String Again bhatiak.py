#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, list):
    powers = []
    total = 2**len(list)

    for i in range(total):
        flag = False
        s = []
        num = ("{0:0%db}" % (len(list))).format(i)

        if("010" in num):
            if len(num) > 3:
                continue
        if len(re.findall("10+1", num)) > 0:
            continue

        for j in range(len(num)):
            if num[j] == '1':
                s.append(list[int(j)])

        # powers.append(s)
        if len(s) == 0:
            continue
        if len(s) == 1:
            powers.append(s)
            # print(num)
        elif len(s) == 2:
            if s[0] == s[1]: 
                powers.append(s)
                # print(num)
        else:
            temp = s[0]
            for i in range(int(len(s)/2)):
                if s[i] != s[len(s)-1-i] or s[i] != temp:
                    flag = True
            if flag==False:
                powers.append(s)
                # print(num)

    # print(powers) 
    return len(powers)  + (len(list) - 2 if len(list) >= 4 else 0)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
