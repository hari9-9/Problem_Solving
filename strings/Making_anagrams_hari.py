import math
import os
import random
import re
import sys
CHARS=26
# Complete the makeAnagram function below.
def makeAnagram(str1,str2):
    c1 = [0]*CHARS 
    c2 = [0]*CHARS 
    #print(c1)
    # count frequency of each character 
    i = 0
    while i < len(str1): 
        c1[ord(str1[i])-ord('a')] += 1
        i += 1
    #print(str1[1])
    #print(ord(str1[0]))
    #print(ord('a'))
    #print(ord(str1[0])-ord('a'))
    i =0
    while i < len(str2): 
        c2[ord(str2[i])-ord('a')] += 1
        i += 1
  
    # traverse count arrays to find  
    # number of characters 
    # to be removed 
    result = 0
    for i in range(26): 
        result += abs(c1[i] - c2[i]) 
    return(result)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = raw_input()

    b = raw_input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
