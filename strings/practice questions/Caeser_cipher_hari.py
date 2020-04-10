#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    final=[]
    if k>26:
        k=(k%26)
    for alpha in s:
        if alpha.isalpha():
            if(alpha.isupper()):
                if(ord(alpha)+k>90):
                    final.append(chr(65+(ord(alpha)+k)-90-1))
                    #print(1,alpha)
                else:
                    final.append(chr(ord(alpha)+k))
                    #print(2,alpha)
            if(alpha.islower()):
                if(ord(alpha)+k>122):
                    final.append(chr(97+(ord(alpha)+k)-122-1))
                    #print(3,alpha)
                else:
                    final.append(chr(ord(alpha)+k))
                    #print(4,alpha)
        else:
            final.append(alpha)
            #print(5,alpha)
        
        #str1 = ''.join(list1)
    print(final)
    return(''.join(final))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
