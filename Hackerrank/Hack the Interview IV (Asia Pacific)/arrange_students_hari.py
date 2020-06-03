#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrangeStudents' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def arrangeStudents(a, b):
    # Write your code here
    a.sort()
    b.sort()
    if len(a)==1:
        return "YES"
    ac=0
    bc=0
    #print(len(a))
    c = [ ]
    d = [ ]
    print(a)
    print(b)
    if(a[0]<b[0]):
        for i in range(len(a)+len(b)):
            if(i%2==0):
                c.append(a[ac])
                ac+=1
            else:
                c.append(b[bc])
                bc+=1
    elif(a[0]>b[0]) :
        for i in range(len(a)+len(b)):
            if(i%2!=0):
                c.append(a[ac])
                ac+=1
            else:
                c.append(b[bc])
                bc+=1
    else:
        for i in range(len(a)+len(b)):
            if(i%2==0):
                c.append(a[ac])
                ac+=1
            else:
                c.append(b[bc])
                bc+=1
        print("c",c)
        ac=0
        bc=0
        for i in range(len(a)+len(b)):
            if(i%2!=0):
                d.append(a[ac])
                ac+=1
            else:
                d.append(b[bc])
                bc+=1
        print("d",d)
        f1=True
        f2=True
        for i in range(len(c)-1):
            if(c[i]<=c[i+1]):
                pass
            else:
                f1=False
            if(d[i]<=d[i+1]):
                pass
            else:
                f2=False
        if((f1 == True) or (f2==True)):
            return "YES"
        else:
            return "NO"
    for i in range(len(c)-1):
        if(c[i]<=c[i+1]):
            continue
        else:
            return "NO"
    return "YES"
        
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = arrangeStudents(a, b)

        fptr.write(result + '\n')

    fptr.close()
